#!/usr/bin/python3
"""Console for executing commands"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __class_names = [
        "BaseModel",
        "User",
        "City",
        "Place",
        "Review",
        "State",
    ]

    def do_EOF(self, line: str) -> bool:
        """EOF command to exit the program"""

        return True

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""

        return True

    def emptyline(self) -> bool:
        return False

    def do_create(self, line: str) -> None:
        try:
            class_name = line.split()[0]
            
            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance = eval(class_name)()
                instance.save()
                print(instance.id)
        except NameError:
                print("** class name missing **")

    def do_show(self, line: str) -> None:
        from models import storage

        try:
            class_name, instance_id = line.split()

            if line.split()[0] not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance_key = class_name + "." + instance_id
                all_instances = storage.all()

                if instance_key not in all_instances:
                    print("** no instance found **")
                else:
                    print(all_instances[instance_key])
        except (ValueError, KeyError):
            if not line:
                print("** class name missing **")
            else:
                print("** instance id missing **")

    def do_destroy(self, line: str) -> None:
        from models import storage

        try:
            class_name, instance_id = line.split()

            if line.split()[0] not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance_key = class_name + "." + instance_id
                all_instances = storage.all()

                if instance_key not in all_instances:
                    print("** no instance found **")
                else:
                    del all_instances[instance_key]
                    storage.save()
        except (ValueError, KeyError):
            if not line:
                print("** class name missing **")
            elif line.split()[0] not in self.__class_names:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_all(self, line: str) -> None:
        from models import storage

        all_instances = storage.all()
        if not line:
            print([str(val) for val in all_instances.values()])
        else:
            class_name = line.split()[0]
            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                class_instances = [str(val) for val in all_instances.values()]
                print(class_instances)

    def do_update(self, line: str) -> None:
        from models import storage

        try:
            class_name, instance_id = line.split()[0], line.split()[1]

            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance_key = class_name + "." + instance_id
                all_instances = storage.all()

                if instance_key not in all_instances:
                    print("** no instance found **")
                else:
                    instance = all_instances[instance_key]
                    attribute = line.split()[2]
                    value = line.split()[3]
                    setattr(instance, attribute, value)
                    instance.save()
        except (KeyError, IndexError):
            if not line:
                print("** class name missing **")
            elif len(line.split()) == 1:
                print("** instance id missing **")
            elif len(line.split()) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
