from rest_framework import serializers
from django.contrib.auth.models import User

from ridemywayapp.models import Rides


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username',
            'email', 'is_staff', 'groups',)


class RidesSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Rides
        fields = (
            'pick_up', 'take_off_time',
            'destination', 'user_id', 'ride_id',)
