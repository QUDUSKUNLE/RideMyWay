from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from ridemywayapp.models import OfferRides, RequestRides


class OfferRidesModelTestCase(TestCase):

    def create_user(self):
        self.name = 'kunle',
        self.password = 'kunle08971',
        self.email = 'kunle@gmail.com'
        return User.objects.create(
                    username=self.name,
                    password=self.password,
                    email=self.email)

    def create_offer_rides(self):
        self.pick_up = '235, Epic Tower, Ikorodu road, Lagos'
        self.take_off_time = '2015-01-05T22:08:37.838Z'
        self.destination = 'Berger'
        self.offer = self.create_user()
        self.created = timezone.now()
        return OfferRides.objects.create(
                        pick_up=self.pick_up,
                        take_off_time=self.take_off_time,
                        destination=self.destination,
                        owner=self.offer,
                        created=self.created)

    def test_offer_rides_creation(self):
        w = self.create_offer_rides()
        self.assertTrue(isinstance(w, OfferRides))
        self.assertEqual(w.pick_up, '235, Epic Tower, Ikorodu road, Lagos')


class RequestRidesTestCase(TestCase):

    def create_user(self):
        self.name = 'kola',
        self.password = 'kola08971',
        self.email = 'kola@gmail.com'
        return User.objects.create(
                    username=self.name,
                    password=self.password,
                    email=self.email)

    def create_offer_rides(self):
        self.pick_up = '235, Epic Tower, Ikorodu road, Lagos'
        self.take_off_time = '2015-01-05T22:08:37.838Z'
        self.destination = 'Berger'
        self.offer = self.create_user()
        self.created = timezone.now()
        return OfferRides.objects.create(
                    pick_up=self.pick_up,
                    take_off_time=self.take_off_time,
                    destination=self.destination,
                    owner=self.offer,
                    created=self.created)
    
    def create_request_ride(self):
        self.user = User.objects.create(
            username='Benin', password='benin08971', email='email@yahoo.com')
        self.offer = self.create_offer_rides()
        return RequestRides.objects.create(
                    owner=self.user,
                    offerrides=self.offer)

    def test_request_ride(self):
        self.request_ride = self.create_request_ride()
        self.assertTrue(isinstance(self.request_ride, RequestRides))
        
