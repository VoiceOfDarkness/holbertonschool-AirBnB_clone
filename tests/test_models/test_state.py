from datetime import datetime
import unittest

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertTrue(hasattr(st, "name"))

    def test_is_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_init(self):
        self.assertIsInstance(self.state, State)

    def test_two_models_are_unique(self):
        st = State()
        self.assertNotEqual(self.state.id, st.id)
        self.assertLess(self.state.created_at, st.created_at)
        self.assertLess(self.state.updated_at, st.updated_at)

    def test_init_args_kwargs(self):
        dt = datetime.utcnow()
        st = State("1", id="5", created_at=dt.isoformat())
        self.assertEqual(st.id, "5")
        self.assertEqual(st.created_at, dt)

    def test_str(self):
        s = self.state.__str__()
        self.assertIn("[State] ({})".format(self.state.id), s)
        self.assertIn("'id': '{}'".format(self.state.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.state.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.state.updated_at)), s)

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertEqual(self.state.id, state_dict["id"])
        self.assertEqual("State", state_dict["__class__"])
        self.assertEqual(self.state.created_at.isoformat(),
                         state_dict["created_at"])
        self.assertEqual(self.state.updated_at.isoformat(),
                         state_dict["updated_at"])


if __name__ == "__main__":
    unittest.main()
