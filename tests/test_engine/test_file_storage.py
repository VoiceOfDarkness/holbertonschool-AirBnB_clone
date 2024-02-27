import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test"
        self.obj.number = 30

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        self.storage.new(self.obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        self.storage.new(self.obj)
        self.assertIn('BaseModel.' + self.obj.id, self.storage.all())

    def test_save(self):
        self.storage.new(self.obj)
        self.storage.save()
        with open("file.json", 'r') as f:
            objects = json.load(f)
        self.assertIn('BaseModel.' + self.obj.id, objects)

    def test_reload(self):
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn('BaseModel.' + self.obj.id, self.storage.all())

