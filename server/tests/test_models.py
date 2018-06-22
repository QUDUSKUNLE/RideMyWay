from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from ridemywayapp.models import Rides


class RidesModelTestCase(TestCase):

    def create_user(self):
        self.name = 'kunle',
        self.password = 'kunle08971',
        self.email = 'kunle@gmail.com'
        return User.objects.create(
                    username=self.name,
                    password=self.password,
                    email=self.email)

    def create_rides(self):
        self.pick_up = '235, Epic Tower, Ikorodu road, Lagos'
        self.take_off_time = '2015-01-05T22:08:37.838Z'
        self.destination = 'Berger'
        self.rider = self.create_user()
        self.created = timezone.now()
        return Rides.objects.create(
                        pick_up=self.pick_up,
                        take_off_time=self.take_off_time,
                        destination=self.destination,
                        rider=self.rider,
                        created=self.created)

    def test_rides_creation(self):
        w = self.create_rides()
        self.assertTrue(isinstance(w, Rides))
