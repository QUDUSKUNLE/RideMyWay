import graphene
from graphene_django import DjangoObjectType

from .models import OfferRides, RequestRides


class OfferRidesType(DjangoObjectType):
    class Meta:
        model = OfferRides


class RequestRidesType(DjangoObjectType):
    
    class Meta:
        model = RequestRides


class Query(graphene.ObjectType):
    offerme = graphene.List(OfferRidesType)
    offerrides = graphene.List(OfferRidesType)

    requestrideme = graphene.Field(RequestRidesType)
    requestrides = graphene.List(RequestRidesType)

    def resolve_offerme(self, info):
        user = info.context.user
        if user.is_authenticated:
            return OfferRides.objects.filter(owner=info.context.user).all()

        return Exception('Authentication credentials were not provided')

    def resolve_offerrides(self, info, **kwargs):
        return OfferRides.objects.all()

    def resolve_requestrideme(self, info):
        user = info.context.user
        if user.is_authenticated:
            return RequestRides.objects.filter(owner=info.context.user).first()

        return Exception('Authentication credentials were not provided')

    def resolve_requestrides(self, info, **kwargs):
        return RequestRides.objects.all()


class CreateOfferRides(graphene.Mutation):
    pick_up = graphene.String(required=True)
    take_off_time = graphene.types.datetime.DateTime()
    destination = graphene.String()
    available_space = graphene.Int()

    class Arguments:
        pick_up = graphene.String(required=True)
        take_off_time = graphene.types.datetime.DateTime()
        destination = graphene.String()
        available_space = graphene.Int()

    def mutate(
        self, info, pick_up,
        take_off_time, destination,
        available_space):
            user = info.context.user
            if user.is_authenticated:
                check_pick_up = OfferRides.objects.filter(
                    owner=info.context.user,
                    pick_up=pick_up).first()
                if check_pick_up:
                    return Exception('Ride already booked')

                offerride = OfferRides(
                    pick_up=pick_up,
                    take_off_time=take_off_time,
                    destination=destination,
                    available_space=available_space,
                    owner=info.context.user
                )

                offerride.save()

                return CreateOfferRides(
                    id=offerride.id,
                    pick_up=offerride.pick_up,
                    take_off_time=offerride.take_off_time,
                    destination=offerride.destination,
                    available_space=offerride.available_space,
                )

            return Exception('Authentication credentials were not provided')


class CreateRequestRides(graphene.Mutation):
    id = graphene.Int()
    offer_id = graphene.Int(required=True)
    pick_up = graphene.String()
    offer_requester = graphene.String()

    class Arguments:
        id = graphene.Int()
        offer_id = graphene.Int(required=True)
        pick_up = graphene.String()
        offer_requester = graphene.String()

    def mutate(self, info, offer_id):
        user = info.context.user

        if user.is_authenticated:
            check_offer = OfferRides.objects.filter(id=offer_id).first()

            if not check_offer:
               return Exception('Offer does not exist')

            request_ride = RequestRides.objects.create(
                owner=user, offerrides=check_offer)

            return CreateRequestRides(
                id=request_ride.id,
                offer_id=check_offer.id,
                pick_up=check_offer.pick_up,
                offer_requester=request_ride.owner.username
            )

        return Exception('Authentication credentials were not provided')


class Mutation(graphene.ObjectType):
    create_offerride = CreateOfferRides.Field()
    create_requestride = CreateRequestRides.Field()
