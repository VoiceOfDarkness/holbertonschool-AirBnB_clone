import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def file_exists(file_name):
    return os.path.exists(file_name)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()
        self.base = BaseModel()
    
    def test_all(self):
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage._FileStorage__objects)
        self.assertEqual(len(obj), 7)

    def test_new(self):
        """Test new method."""
        bm = BaseModel()
        self.storage.new(bm)
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store.keys())
        self.assertIn(self.base, store.values())
