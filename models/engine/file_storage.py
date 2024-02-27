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
            json_file = ""
            try:
                with open(FileStorage.__file_path, "r") as my_file:
                    json_file = json.loads(my_file.read())
                    for key in json_file:
                        FileStorage.__objects[key] = my_dict[json_file[key]['__clas\
    s__']](**json_file[key])
            except:
                pass
