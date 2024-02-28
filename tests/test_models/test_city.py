from datetime import datetime
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self) -> None:
        self.user = City()

    def test_attributes(self):
        city = City()
        self.assertEqual(str, type(city.id))
        self.assertEqual(datetime, type(city.created_at))
        self.assertEqual(datetime, type(city.updated_at))
        self.assertTrue(hasattr(city, "__tablename__"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))
