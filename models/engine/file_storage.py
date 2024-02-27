import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        with open(self.__file_path, "r") as file:
            self.__objects = json.load(file)

