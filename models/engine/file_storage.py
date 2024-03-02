"""
This module contains the FileStorage class, which is responsible for
serializing and deserializing instances to and from a JSON file. It also
stores all the instances created.
"""
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """
    This class is responsible for serializing and deserializing instances
    to and from a JSON file. It also stores all the instances created.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""

        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """

        try:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    class_name = value["__class__"]
                    self.__objects.update({key: classes[class_name](**value)})

        except FileNotFoundError:
            pass
