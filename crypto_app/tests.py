from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Organization, CryptoPrice

class OrganizationTestCase(TestCase):
    def setUp(self):
        Organization.objects.create(name="Test Org")

    def test_organization_creation(self):
        org = Organization.objects.get(name="Test Org")
        self.assertEqual(org.name, "Test Org")

class CryptoPriceTestCase(TestCase):
    def setUp(self):
        org = Organization.objects.create(name="Test Org")
        CryptoPrice.objects.create(org=org, symbol="BTC", price=50000)

    def test_crypto_price_creation(self):
        price = CryptoPrice.objects.get(symbol="BTC")
        self.assertEqual(price.symbol, "BTC")
