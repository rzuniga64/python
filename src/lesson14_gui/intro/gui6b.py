from sys import exit
from tkinter import *                    # get Tk widget classes
from gui6 import Hello                   # get the subframe class

parent = Frame(None)                     # make a container widget
parent.pack()
# The button on the right in this window represents an embedded component
# its button really represents an attached Python class object
Hello(parent).pack(side=RIGHT)           # attach Hello instead of running it

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
