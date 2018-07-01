from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ridemywayapp.models import RequestRides, OfferRides


User = get_user_model()
client = APIClient()


class RequestRidesTestCase(TestCase):
    
    def setUp(self):
        self.admin = User.objects.create_superuser(
            email='admin@admin.com', password='devpassword',
            username='admin')
        self.token_admin = "tokenadmin"
        self.user = User.objects.create_user(
            email='admin1@admin.com', password='devpassword1',
            username='admin1')
        self.token_user = 'testtoken'
        self.other_user = User.objects.create_user(
            email='admin2@admin.com', password='devpassword2',
            username='admin2')
        self.token_other_user = 'otherusertesttoken'
        self.offer_rides_1 = OfferRides.objects.create(
            pick_up='Epic tower', take_off_time='2015-01-05T22:08:37.838Z',
            destination='Berger', owner=self.user, available_space=5)
        self.request_rides = RequestRides.objects.create(
            owner=self.other_user, offerrides=self.offer_rides_1)
        self.request_rides_url = '/api/offer-rides/'

    def test_no_offer_rides_created(self):
        response = client.get(self.request_rides_url, format='json')
        self.assertEqual(response.data['results'][0]['pick_up'], 'Epic tower')
        self.assertEqual(response.data['count'], 1)

    def test_create_offer_rides(self):
        test_create_offer_rides = OfferRides(
            pick_up='Epic tower, Ikorodu, Lagos',
            take_off_time='2018-01-05T22:08:37.838Z',
            destination='Olowora, Berger, Lagos',
            owner=self.other_user,
            available_space=4)
        test_create_offer_rides.save()

        response = client.get(self.request_rides_url, format='json')
        self.assertEqual(response.data['count'], 2)
