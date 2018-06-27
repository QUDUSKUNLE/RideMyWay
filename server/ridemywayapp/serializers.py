from rest_framework import serializers
from django.contrib.auth.models import User
from ridemywayapp.models import OfferRides, RequestRides


class UserSerializer(serializers.ModelSerializer):
    offer_rides = serializers.PrimaryKeyRelatedField(
        many=True, queryset=OfferRides.objects.all())

    class Meta:
        model = User
        fields = (
            'id', 'username', 'offer_rides',)


class OfferRidesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = OfferRides
        fields = (
            'pick_up', 'take_off_time',
            'destination', 'offer_id', 'created', 'owner',)


class RequestRidesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    pick_up = serializers.ReadOnlyField(
        source='offerrides.pick_up')
    destination = serializers.ReadOnlyField(
        source='offerrides.destination')
    take_off_time = serializers.ReadOnlyField(
        source='offerrides.take_off_time')

    class Meta:
        model = RequestRides
        fields = (
            'request_id', 'owner', 'created',
            'offerrides', 'pick_up', 'destination', 'take_off_time',)
