from datetime import datetime
import unittest

from models.state import State


class Teststate(unittest.TestCase):
    def setUp(self) -> None:
        self.user = State()

    def test_attributes(self):
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertTrue(hasattr(st, "name"))
