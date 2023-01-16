from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        #Creating new user with email succesfull
        email = 'test12@gmail.com'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        #Creating new user with email lowercase
        email = 'test12@KAKUKI.com'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email.lower())

    def test_create_user_email_normalized(self):
        #Raise error with no email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email = None,
                password = 'test1234'
            )

    def test_create_new_superuser(self):
        #Test creating a new super user
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)