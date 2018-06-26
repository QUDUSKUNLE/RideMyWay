from django.test import TestCase
from utils.unique_id import PushID

class UniqueIDTestCase(TestCase):
    
    def create_id(self):
        self.unique_id = PushID().next_id()
        return self.unique_id

    def test_unique_id(self):
        self.id = self.create_id()
        self.assertTrue(type(self.id), 'string')
