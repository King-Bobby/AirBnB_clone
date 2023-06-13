#!/usr/bin/python3
"""
Using Module Cmd and
Module Console containing class HBNBCommand
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class cmd"""
    prompt = '(hbnb) '
    __valid_classes = ["BaseModel", "User", "Place",
                       "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Same function as Quit"""
        return True

    def emptyline(self):
        """Does Nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class"""
        command = line.split(" ")
        if command[0] == "":
            print("** class name missing **")
        elif command[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        else:
            if command[0] == "BaseModel":
                x = BaseModel()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
