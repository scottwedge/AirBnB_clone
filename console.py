#!/usr/bin/python3
"""
Console that is the entry point of the program
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Class for HBNB command
    """
    use_rawinput = False

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review}

    def do_create(self, line):
        """Create instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
            print("** class doesn't exist **")
        else:
            if line in self.classes:
                inst = self.classes[line]
                new_instance = inst()
                print(new_instance.id)
                new_instance.save()
                self.count += 1
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show instance of BaseModel"""
        arg = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            if arg[0] in self.classes:
                storage = FileStorage()
                dict1 = storage.all()
                list_obj = list(dict1.values())
                flag = 0
                for obj in list_obj:
                    instance = eval(arg[0])
                    if obj.id == arg[1] and instance == obj.__class__:
                        print(obj)
                        flag = 1
                if flag == 0:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy instance of BaseModel"""
        arg = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            dict1 = storage.all()
            key = arg[0] + "." + arg[1]
            obj = dict1.get(key)
            if obj is not None:
                instance = eval(arg[0])
                if obj.id == arg[1] and instance == obj.__class__:
                    del dict1[key]
                else:
                    print("** no instance found **")
                storage.save()
            elif arg[0] in self.classes:
                print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Display all instances """
        if line in self.classes or line == "":
            storage = FileStorage()
            dict1 = storage.all()
            list_obj = []
            for key, val in dict1.items():
                if line != "":
                    instance = eval(line)
                    if val.__class__ == instance:
                        list_obj.append(str(val))
                else:
                    list_obj.append(str(val))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instances of BaseModel"""
        arg = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            if arg[0] in self.classes:
                storage = FileStorage()
                storage.reload()
                dict1 = storage.all()
                key = arg[0] + "." + arg[1]
                obj = dict1.get(key)
                if obj is not None:
                    instance = eval(arg[0])
                    if obj.id == arg[1] and instance == obj.__class__:
                        setattr(obj, arg[2], arg[3])
                        dict1[key] = obj
                        storage.save()
                    else:
                        print("** no instance found **")
                elif arg[0] in self.classes:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """
        empty line
        """
        pass

    def default(self, line):
        "Default method for line"
        arg = shlex.split(line)
        if arg[0] in self.classes:
            if arg[1] == "all()":
                command = arg[0]
                self.do_all(command)
            elif arg[1] == "count()":
                command = eval(arg[0])
                storage = FileStorage()
                dict1 = storage.all()
                count = 0
                for key, val in dict1.items():
                    if command == val.__class__:
                        count += 1
                print(count)
            else:
                print("*** Unknown syntax:", line)


        else:
            print("*** Unknown syntax:", line)


    def do_quit(self, line):
        """Quit command to exit the program

        """
        sys.exit(1)

    def do_EOF(self, line):
        """
         Exit
        """
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
