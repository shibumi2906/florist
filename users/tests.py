# users/tests.py

from django.test import TestCase

class UsersTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(2 * 2, 4)

