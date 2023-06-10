#!/usr/bin/python3

"""
Module Console containing class HBNBCommand
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class cmd"""
    prompt = '(hbnb) '
    __valid_classes = ["BaseModel"]

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

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        command = line.split(" ")
        if command[0] == "":
            print("** class name missing **")
        elif command[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        
        // still testing//
        
        elif command[1] == 1:
            print("** instance id missing **")
        elif command[1] not in self.__valid_classes.id:
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
