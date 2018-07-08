import graphene
from graphene_django import DjangoObjectType

from .models import OfferRides, RequestRides


class OfferRidesType(DjangoObjectType):
    class Meta:
        model = OfferRides


class Query(graphene.ObjectType):
    offerme = graphene.List(OfferRidesType)
    offerrides = graphene.List(OfferRidesType)


    def resolve_offerme(self, info):
        user = info.context.user
        if user.is_authenticated:
            return OfferRides.objects.filter(owner=info.context.user).all()
        
        return Exception('Authentication credentials were not provided')

    def resolve_offerrides(self, info, **kwargs):
        return OfferRides.objects.all()


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

    
    def mutate(self, info, pick_up, take_off_time, destination, available_space):
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
        raise Exception('Authentication credentials were not provided')


class Mutation(graphene.ObjectType):
    create_offerride = CreateOfferRides.Field()
