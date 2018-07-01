
from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ridemywayapp.models import RequestRides, OfferRides


User = get_user_model()
client = APIClient()

class APIRootTestCase(TestCase):
    
    def setUp(self):
        self.request_rides_url = '/'

    def test_no_offer_rides_created(self):
        response = client.get(self.request_rides_url, format='json')
        self.assertEqual(response.data['users'], 'http://testserver/api/users/')
        self.assertEqual(type(response.data), dict)
