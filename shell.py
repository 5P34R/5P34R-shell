from cmd import Cmd
import os


class spear(Cmd):
    intro = "5P34R shell"
    prompt = '(5P34R) => '
                           

    def default(self, arg):
        if arg in ['quit', 'q', 'close', 'exit']:
            self.close()
        else:
            print(os.system(arg)) 
        
        
    def close(self):    
        print("Exiting...")
        exit()

shell = spear()
shell.cmdloop()

