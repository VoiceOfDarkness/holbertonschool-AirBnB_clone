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
    
    def test_all(self):
        obj1 = BaseModel()
        obj1.id = "1"
        obj2 = BaseModel()
        obj2.id = "2"

        self.assertEqual(self.storage.all(), {"BaseModel.1": obj1, "BaseModel.2": obj2})
