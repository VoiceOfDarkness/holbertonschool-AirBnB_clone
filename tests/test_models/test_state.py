from datetime import datetime
import unittest

from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, State)

    def test_name_property(self):
        name = "Test State"
        self.state.name = name
        self.assertEqual(self.state.name, name)
