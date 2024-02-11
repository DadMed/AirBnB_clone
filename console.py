#!/usr/bin/python3
"""
 Quit command to exit the program.
"""
import  cmd

class HBNBCommand(cmd.Cmd):
    """
     Quit command to exit the program.
    """

    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True
    
    def help_quit(self, arg):
        """
         Quit command to exit the program.
        """
        print("Qiut command to exit the program")
    
    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()