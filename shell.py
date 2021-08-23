from cmd import Cmd
import os


class spear(Cmd):
    intro = "5P34R shell"
    prompt = '(5P34R) => '
    
    def default(self, arg):
        print(os.system(arg))


shell = spear()
shell.cmdloop()
