from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_check_user_with_email(self):

        email = "email@example.com"
        password = "example_password"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            is_active=False,
            is_staff=True
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.is_active,False)
        self.assertEqual(user.is_staff,True)

    def test_new_user_email_normalized(self):
        """ test email normalized for new users"""

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email,"sample123")

            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raise_error(self):
        """ test user with out email address"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("","2333")


    def test_create_superuser(self):
        """ test super user method"""

        user = get_user_model().objects.create_superuser(
            "email@example.com","pass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


