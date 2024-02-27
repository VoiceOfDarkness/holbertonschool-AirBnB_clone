#!/usr/bin/python3
"""Console for executing commands"""
import cmd
import json

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line: str) -> bool:
        """EOF command to exit the program"""

        return True

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""

        return True

    def emptyline(self) -> bool:
        return False

    def do_create(self, line: str) -> None:
        from models import storage

        if not line:
            print("** class name missing **")
        else:
            try:
                instance = eval(line)()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line: str) -> None:
        from models import storage

        try:
            class_name, instance_id = line.split()
            instance = storage.all()[class_name + "." + instance_id]
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except ValueError:
            if not line:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line: str) -> None:
        from models import storage

        try:
            class_name, instance_id = line.split()
            instance = storage.all()[class_name + "." + instance_id]
            if instance:
                del storage.all()[class_name + "." + instance_id]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            if not line:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, line: str) -> None:
        from models import storage

        if not line:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                class_name = line.split()[0]
                print(
                    [
                        str(value)
                        for key, value in storage.all().items()
                        if class_name in key
                    ]
                )
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, line: str) -> None:
        from models import storage

        try:
            class_name, isinstance_id = line.split()[0], line.split()[1]
            instance = storage.all()[class_name + "." + isinstance_id]
            if not instance:
                print("** no instance found **")
            else:
                attribute = line.split()[2]
                value = line.split()[3]
                setattr(instance, attribute, value)
                instance.save()
        except KeyError:
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
