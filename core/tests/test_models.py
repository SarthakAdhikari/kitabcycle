from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests (TestCase):
    def test_create_user_with_email_sucessful(self):
        '''Test creating a new user with email is successful.'''
        email = "test@exampl.com"
        password = "test@123user"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalized(self):
        '''Test that email of new user is normalized.'''
        email = "test@EXAMPLE.COM"
        password = "test@123user"
        created_user = get_user_model().objects.create_user(email=email,
                                                        password=password)
        self.assertEqual(created_user.email, email.lower())

    def test_create_user_with_invalid_email(self):
        '''Test that creating user without email raises an error.'''
        with self.assertRaises(ValueError):
            password = "test@123user"
            created_user = get_user_model().objects.create_user(email=None,
                                                        password=password)
    def test_create_user_with_profile_sucessful(self):
        created_user = get_user_model()(email="asd@asd.com", password="password123")
        self.assertTrue(hasattr(created_user, 'profile_set'))
