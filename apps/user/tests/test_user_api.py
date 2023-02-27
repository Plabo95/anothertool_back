from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    #Helper function cause its repetitive
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    #Not needed to be authenticated

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        "Test creating valid payload user is successfull"
        payload = {
            'email': 'test@kakuki.com',
            'password': 'pichurrio1234'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        "Test creating a user that already exists"
        payload = {'email': 'test@kakuki.com','password': 'pichurrio1234'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        "Test password should be more than 5 chars"
        payload = {'email': 'test@kakuki.com','password': 'kk'}

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


