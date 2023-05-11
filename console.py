#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
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
        """Creates a new instance"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
