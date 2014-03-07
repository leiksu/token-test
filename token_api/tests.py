from django.test import TestCase
from django.test.client import Client
import unittest
from models import ClientData
import uuid

class BasicDataTestCase(TestCase, unittest.TestCase):
    
    def setUp(self):
        # Initialize a Django test client
        self.client = Client()
   
        
    def testRetriveData(self):
        # generate tmp token
        tmp_token = uuid.uuid4().hex
        tmp_key = "tmp_key"
        tmp_value = "tmp_value"

        ClientData.objects.create(
                                  token = tmp_token,
                                  client_key = tmp_key,
                                  client_value = tmp_value
                                  )
        
        response = self.client.get('/retrieve_data/%s/%s' % (tmp_token, tmp_key))
        self.assertEqual(response.status_code, 200, "Testing returned client key")

        response = self.client.get('/retrieve_data/%s/' % tmp_token)
        self.assertEqual(response.status_code, 200, "Testing returned client key")
        
        