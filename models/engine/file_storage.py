import json

from models.base_model import BaseModel
from models.user import User


classes = {
    "BaseModel": BaseModel,
    "User": User,
}

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                # Requirements: 1. Get class name (__class__ attribute from json)
                #  self.__objects = {k: classes[](**v) for k, v in json.load(f).items()}
                for key, value in json.load(f).items():
                    class_name = value["__class__"]
                    self.__objects.update({key: classes[class_name](**value)})

        except FileNotFoundError:
            pass
