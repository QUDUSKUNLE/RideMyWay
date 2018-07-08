from rest_framework import serializers
from django.contrib.auth.models import User
from ridemywayapp.models import OfferRides, RequestRides


class UserSerializer(serializers.ModelSerializer):
    
    """
        Class UserSerializer serializer
    """

    offer_rides = serializers.PrimaryKeyRelatedField(
        many=True, queryset=OfferRides.objects.all())

    class Meta:
        model = User
        fields = (
            'id', 'username', 'offer_rides',)


class OfferRidesSerializer(serializers.ModelSerializer):
    
    """
        Class OfferRidesSerializer serializer
    """
    class Meta:
        model = OfferRides
        fields = (
            'id', 'pick_up', 'take_off_time',
            'destination', 'created', 'owner', 'available_space')


class RequestRidesSerializer(serializers.ModelSerializer):

    """
        Class RequestRidesSerializer serializer
    """

    pick_up = serializers.ReadOnlyField(
        source='offerrides.pick_up')
    destination = serializers.ReadOnlyField(
        source='offerrides.destination')
    take_off_time = serializers.ReadOnlyField(
        source='offerrides.take_off_time')

    class Meta:
        model = RequestRides
        fields = (
            'id', 'owner', 'created',
            'offerrides', 'pick_up', 'destination', 'take_off_time',)
