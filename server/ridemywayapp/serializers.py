from rest_framework import serializers
from django.contrib.auth.models import User
from ridemywayapp.models import OfferRides, RequestRides


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'url', 'password',)


class OfferRidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfferRides
        fields = (
            'pick_up', 'take_off_time',
            'destination', 'offer_id', 'created', 'user',)


class RequestRidesSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = RequestRides
        fields = ('request_id', 'user_id', 'offer', 'created',)
