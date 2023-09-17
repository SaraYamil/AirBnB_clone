#!/usr/bin/python3

"""airbnb clon  - ndiro liha bhal comande line module"""

import cmd
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage
from models.city import City
from models.amenity import Amenity
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ Holberton command prompt bach ndkhlo lmdl data """
    prompt = '(hbnb) '
    class_names = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "User": User,
        "Review": Review
    }

    def default(self, arg):
        """
        dddd,,,,,,,,,,,,, dkkkkkkkkkk dkdk k dk,odld,koldlkd,k,do,lkkddddd
        ddddddddddddddddddddd ,dddddddddddddddddddddd dddddddddddddddddd
        returdd.
        """
        methods_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        commands = arg.strip().split(".")
        if len(commands) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = commands[0]
        command = commands[1].split("(")[0]
        line = ""
        if (command == "update" and commands[1].split("(")[1][-2] == "}"):
            inputs_data = commands[1].split("(")[1].split(",", 1)
            inputs_data[0] = shlex.split(inputs_data[0])[0]
            line = "".join(inputs_data)[0:-1]
            line = class_name + " " + line
            self.do_update_using_class(line.strip())
            return
        try:
            inputs_data = commands[1].split("(")[1].split(",")
            for n in range(len(inputs_data)):
                if (n != len(inputs_data) - 1):
                    line = line + " " + shlex.split(inputs_data[n])[0]
                else:
                    line = line + " " + shlex.split(inputs_data[n][0:-1])[0]
        except IndexError:
            inputs_data = ""
            line = ""
        line = class_name + line
        if (command in methods_dict.keys()):
            methods_dict[command](line.strip())

    def do_quit(self, arg):
        """
        dddddddddddddddddddddddddddddddd

        ddddddddddd

        vvvvvvv
            vvve
        """
        return True

    def do_EOF(self, arg):
        """
        ddddddd ddddddddddd ddddddddddd dddddddddd dddddddddd ddddddddddd

        ddddddddddddd CTRL+D

        ccccccc
            True
        """
        print("")
        return True

    def emptyline(self):
        """
        vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv.

        vvvvvvvvvvvvvvvvvvvvvvvvvvv vvvvvvvvvvvvvv vvvvvvvvv vvvvvvvty
        combbbbbbbbbbed.

        vvvvvvv
            nnnn
        """
        pass

    def do_nothing(self, arg):
        """ vvvvvvvthing """
        pass

    def do_create(self, arg):
        """
        bbbbbbbbbb bbbbbbbbbbbbb bbbbbbbbbbb bbbbbbbbbb bbbbbbbbbbbbbbb)
        bbbbbbbbbbbbbbbbb

        Usage: bbbbbe <class name>

        Args:
            arg (strbbbbbbbbbbbbbbbbbbbbbbbbbbbbe to create

        Return:
            walo
        """
        if not arg:
            print("** class name missing **")
            return
        line = shlex.split(arg)
        if line[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        new_inst = HBNBCommand.class_names[line[0]]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """
        Pccccccc ccccccccccepresccccccc ccccccc cccc ccccc cccccccc cccccs
        xxxxx xxxid

        Usage: wwwwwwwwwwwwwwwwwwwwww

        Args:
            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxxw

        Return:
            walo
        """
        command_args = shlex.split(arg)
        if len(command_args) == 0:
            print("** class name missing **")
            return
        if command_args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(command_args) <= 1:
            print("** instance id missing **")
            return
        inst_dicts = storage.all()
        key = "{}.{}".format(command_args[0], command_args[1])
        if key in inst_dicts:
            obj_instance = str(inst_dicts[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
        ffffffffffffffffff)

        fffffffffffffffffffffffffffffff>

        Args:
            argffffffffffffffffffffffffffffffffffv ffffffffffffffff

        Return:
            walo
        """
        command_args = shlex.split(arg)
        if len(command_args) == 0:
            print("** class name missing **")
            return
        if command_args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(command_args) <= 1:
            print("** instance id missing **")
            return
        inst_dicts = storage.all()
        key = "{}.{}".format(command_args[0], command_args[1])
        if key in inst_dicts:
            del inst_dicts[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        dddddddddddd ddddddddddd ddddddddddd ddddddddddddd dddddddddd ddd ddd
        cccccccccc

        Usage: ccccccccccccccccccccccc

        Args:
            cccccccccccccccccccccccccccccccccccccccccccccccccccccing
        """
        json_data = []
        inst_dicts = storage.all()
        if not arg:
            for key in inst_dicts:
                json_data.append(str(inst_dicts[key]))
            print(json.dumps(json_data))
            return
        command_arg = shlex.split(arg)
        if command_arg[0] in HBNBCommand.class_names.keys():
            for key in inst_dicts:
                if command_arg[0] in key:
                    json_data.append(str(inst_dicts[key]))
            print(json.dumps(json_data))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Args:
            arg (str): class name, id, attribute name and attribute value of
            the instance to update
        """
        if not arg:
            print("** class name missing **")
            return
        command_arg = shlex.split(arg)
        insts_dicts = storage.all()
        if command_arg[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if (len(command_arg) == 1):
            print("** instance id missing **")
            return
        try:
            key = command_arg[0] + "." + command_arg[1]
            insts_dicts[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(command_arg) == 2):
            print("** attribute name missing **")
            return
        if (len(command_arg) == 3):
            print("** value missing **")
            return
        inst = insts_dicts[key]
        if hasattr(inst, command_arg[2]):
            data_type = type(getattr(inst, command_arg[2]))
            setattr(inst, command_arg[2], data_type(command_arg[3]))
        else:
            setattr(inst, command_arg[2], command_arg[3])
        storage.save()

    def do_update_using_class(self, arg):
        """
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xxxxxxxxxxxxx
        wwwwwwwwwwww wwwwwwwwwwwwwwwwwww wwwwwwwwwwwwwwww wwwww
        """
        if not arg:
            print("** class name missing **")
            return
        dictionary_data = "{" + arg.split("{")[1]
        data_arg = shlex.split(arg)
        objs_dict = storage.all()
        if data_arg[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if (len(data_arg) == 1):
            print("** instance id missing **")
            return
        try:
            key = data_arg[0] + "." + data_arg[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (dictionary_data == "{"):
            print("** attribute name missing **")
            return

        dictionary_data = dictionary_data.replace("\'", "\"")
        dictionary_data = json.loads(dictionary_data)
        inst = objs_dict[key]
        for my_key in dictionary_data:
            if hasattr(inst, my_key):
                data_type = type(getattr(inst, my_key))
                setattr(inst, my_key, dictionary_data[my_key])
            else:
                setattr(inst, my_key, dictionary_data[my_key])
        storage.save()

    def do_count(self, arg):
        """
        cccccccccccccccccccccccccccccc ccccccccccss

        Usage: <class name>.count()

        Args:
            arg (str): class name of the instance to count
        """
        counter = 0
        objects_dict = storage.all()
        for key in objects_dict:
            if (arg in key):
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
