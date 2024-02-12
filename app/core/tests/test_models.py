from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_check_user_with_email(self):

        email = "email@example.com"
        password = "example_password"

        user = get_user_model.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))