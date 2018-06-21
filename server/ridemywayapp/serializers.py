from rest_framework import serializers
from django.contrib.auth.models import User

from ridemywayapp.models import Rides


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups',)


class RidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rides
        fields = ('pick_up', 'take_off_time', 'destination', 'rider', 'ride_id')
