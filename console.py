import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_EOF(self, line: str) -> bool:
        """EOF command to exit the program"""
        
        return True
    
    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""
        
        return True
    
    def emptyline(self) -> bool:
        return False
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
