import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        temp = {}
        for key, value in self.__objects.items():
            temp.update({key: value.to_dict()})
        json_file = json.dumps(temp)
        with open(self.__file_path, "w") as file:
            file.write(json_file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                json_file = json.load(file)
                self.__objects = {key: BaseModel(**value) for key, value in json_file.items()}

        except:
            pass
