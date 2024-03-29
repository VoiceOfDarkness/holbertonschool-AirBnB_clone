#!/usr/bin/python3
"""Console for executing commands"""
import cmd
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command line interpreter\n
    """

    prompt = "(hbnb) "
    __class_names = [
        "BaseModel",
        "User",
        "City",
        "Place",
        "Review",
        "State",
        "Amenity",
    ]

    def do_EOF(self, line: str) -> bool:
        """EOF command to exit the program\n"""

        return True

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""

        return True

    def emptyline(self) -> bool:
        """Called when an empty line is entered in response to the prompt\n"""

        return False

    def do_create(self, line: str) -> None:
        """Create a new instance of BaseModel,
        save it (to the JSON file) and print the id\n"""

        try:
            class_name = line.split()[0]

            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance = eval(class_name)()
                instance.save()
                print(instance.id)
        except (NameError, IndexError):
            print("** class name missing **")

    def do_show(self, line: str) -> None:
        """Show the string representation of an instance
        based on the class name and id\n"""

        from models import storage

        try:
            class_name = line.split()[0]

            if line.split()[0] not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance_id = line.split()[1]
                instance_key = class_name + "." + instance_id
                all_instances = storage.all()

                if instance_key not in all_instances:
                    print("** no instance found **")
                else:
                    print(all_instances[instance_key])
        except (IndexError, KeyError):
            if not line:
                print("** class name missing **")
            else:
                print("** instance id missing **")

    def do_destroy(self, line: str) -> None:
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)\n"""

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
        """Prints all string representation of all
        instances based or not on the class name\n"""

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
        """Updates an instance based on the class name andid by
        adding or updating attribute (save the change into the JSON file)\n"""

        from models import storage

        try:
            class_name = line.split()[0]

            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                instance_id = line.split()[1]

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

    def default(self, line: str) -> None:
        """Called on an input line when the
        command prefix is not recognized\n"""

        from models import storage

        user_input = line.split(".")

        try:
            if user_input[1] == "all()":
                self.do_all(user_input[0])
            elif user_input[1] == "count()":
                count = 0
                for key in storage.all().keys():
                    if user_input[0] in key:
                        count += 1
                print(count)
            elif user_input[1].startswith("show"):
                instance_id = user_input[1].split("(")[1].split(")")[0]
                self.do_show(user_input[0] + " " + instance_id)
            elif user_input[1].startswith("destroy"):
                instance_id = user_input[1].split("(")[1].split(")")[0]
                self.do_destroy(user_input[0] + " " + instance_id)
            elif user_input[1].startswith("update"):

                if "{" in user_input[1] and "}" in user_input[1]:
                    update_context = user_input[1].replace("'", '"')
                    instance_id = update_context.split("(")[1]\
                                                .split(",")[0].strip('"')
                    dict_start = update_context.find("{")
                    dict_end = update_context.find("}") + 1
                    update_context = json.\
                        loads(update_context[dict_start:dict_end])

                    for key, value in update_context.items():
                        self.do_update(
                            user_input[0]
                            + " "
                            + instance_id
                            + " "
                            + key
                            + " "
                            + str(value)
                        )
                else:
                    update_context = user_input[1].split("(")[1].split(")")[0]
                    values = update_context.split(", ")
                    instance_id = values[0].strip('"')
                    attribute_name = values[1].strip('"')
                    attribute_value = values[2].strip('"')

                    self.do_update(
                        user_input[0]
                        + " "
                        + instance_id
                        + " "
                        + attribute_name
                        + " "
                        + str(attribute_value)
                    )
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
