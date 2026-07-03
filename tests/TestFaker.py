import unittest
from faker import Faker

class TestFaker(unittest.TestCase):

    def test__Faker(self):
        fake = Faker("en_IN")
        self.assertIsNotNone(fake)

        #fake.randint(1, 100)
        self.assertIsNotNone(fake.email())
        self.assertIsNotNone(fake.country())
        self.assertIsNotNone(fake.name())
        self.assertIsNotNone(fake.text())
        self.assertIsNotNone(fake.latitude())
        self.assertIsNotNone(fake.longitude())
        self.assertIsNotNone(fake.url())
        self.assertIsNotNone(fake.address())
        self.assertIsNotNone(str(fake.latitude()))
        self.assertIsNotNone(str(fake.longitude()))
        self.assertIsNotNone(fake.city())
        self.assertIsNotNone(fake.postcode())
        self.assertIsNotNone(fake.currency())
        self.assertIsNotNone(fake.currency_code())
        self.assertIsNotNone(fake.currency_name())
        
        