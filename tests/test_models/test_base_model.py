import unittest

from datetime import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.model.created_at = datetime.now()
        self.model.updated_at = datetime.now()
        self.storage = FileStorage()
        self.storage.reload()

    def test_id(self):
        self.model_test = BaseModel()
        self.assertNotEqual(self.model.id, self.model_test.id)

    def test_save(self):
        old_updated_at = self.model.updated_at
        old_storage_updated_at = self.storage.all()[f"BaseModel.{self.model.id}"].updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        new_strage_updated_at = self.storage.all()[f"BaseModel.{self.model.id}"].updated_at
        self.assertNotEqual(old_storage_updated_at, new_strage_updated_at)

    def test_to_dict(self):
        result = self.model.to_dict()
        self.assertEqual(result["__class__"], self.model.__class__.__name__)
        self.assertEqual(result["created_at"], self.model.created_at.isoformat())
        self.assertEqual(result["updated_at"], self.model.updated_at.isoformat())

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)
