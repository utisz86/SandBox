# https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

from tkinter import Tk, Label, Button, LEFT, RIGHT, W

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        

        self.label = Label(master, text="This is out first GUI")
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)

        master.bind("<Button-1>", self.click())

    def greet(self):
        print("Greetings!")

    def click(self):
        print(self)


     

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

