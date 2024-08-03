# catalog/tests.py

from django.test import TestCase

class CatalogTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(1 + 1, 2)

