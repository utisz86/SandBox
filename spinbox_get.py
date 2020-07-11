from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class Root(Tk):
    new_variable

    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Spin Box")
        self.minsize(640, 400)
        
 
        self.spinBox()    

    def spinCallBack(self):
        value = self.spin.get()
        print(value)
        

    def spinBox(self):
        self.spin = ttk.Spinbox(self, from_ = 0, to = 10, command = self.spinCallBack)
        self.spin.grid(column = 0, row = 2)
 
 

root = Root()
root.mainloop()        