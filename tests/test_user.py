import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()

    def test_user_email(self):
        self.user.email = 'maga@gmail.com'
        self.assertEqual(self.user.email, "maga@gmail.com")

    def test_user_password(self):
        self.user.password = 'test_password'
        self.assertEqual(self.user.password, "test_password")

    def test_user_first_name(self):
        self.user.first_name = 'test_first_name'
        self.assertEqual(self.user.first_name, "test_first_name")

    def test_user_last_name(self):
        self.user.last_name = 'test_last_name'
        self.assertEqual(self.user.last_name, "test_last_name")
