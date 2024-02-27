import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

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
                for elem in json.load(file).values():
                    name = elem["__class__"]
                    del elem["__class__"]
                    self.new(eval(name)(**elem))

        except FileNotFoundError as e:
            pass
