from datetime import datetime
import unittest

from models.state import State


class Teststate(unittest.TestCase):
    def setUp(self) -> None:
        self.user = State()

    def test_attributes(self):
        state = State()
        self.assertEqual(str, type(state.id))
        self.assertEqual(datetime, type(state.created_at))
        self.assertEqual(datetime, type(state.updated_at))
        self.assertTrue(hasattr(state, "name"))
