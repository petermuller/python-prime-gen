"""
interface.py

Classes for interacting with the prime number generator.

@author Peter Muller (pmm5983@rit.edu)
"""

import Tkinter

class CLIInterface:
    """
    Command line wrapper class for interaction with the prime number generator.
    """
    
    def __init__(self,prime):
        self.prime = prime
        
    #TODO reimplement as state machine to get rid of nested while loops
    def prompt(self):
        """
        Main program flow for the CLI
        """
        run = True
        while (run):
            try:
                number = int(input("Enter a value of N to find the Nth prime" +
                    \ "number: "))
                result = self.prime.getNthPrime(number)
                print(str(result))
            except:
                print("Error, please enter a positive integer.")
            print
            again = raw_input("Type 'e' to exit, or press Enter to try " + 
                \ "again. ").strip()
            if again == 'e':
                run = False
            print
    
class GUIInterface:
    """
    Graphical wrapper class for interaction with the prime number generator.
    """
    
    def __init__(self,prime,master=None):
        #TODO cleanup, if possible?
        #TODO make windows more user-friendly.
        self.prime = prime
        master.title("Petulant-Octo-Bear")
        master.minsize(100,100)
        self.input = Tkinter.Entry(master)
        self.input.insert(Tkinter.INSERT, "Enter a number N for the Nth prime number")
        self.input.pack(fill='x')
        self.f = Tkinter.Frame(master)
        self.f.pack()
        self.submit = Tkinter.Button(self.f,text="Submit",command=self.submit)
        self.submit.pack(side=Tkinter.LEFT)
        self.ex = Tkinter.Button(self.f,text="Exit",command=self.quit)
        self.ex.pack(side=Tkinter.LEFT)
        self.answer = Tkinter.Text(master,height=1)
        self.answer.pack(fill='x')
        self.master = master
        
    def submit(self):
        """
        Gets input and sets the output
        """
        try:
            number = int(self.input.get().strip())
            if number < 1:
                raise
            self.answer.delete('1.0','2.0')
            self.answer.insert(Tkinter.INSERT,str(self.prime.getNthPrime(number)))
        except:
            self.answer.delete('1.0','2.0')
            self.answer.insert(Tkinter.INSERT,"Error, please enter a positive integer.")
        
    def quit(self):
        """
        Exits the program
        """
        self.master.destroy()