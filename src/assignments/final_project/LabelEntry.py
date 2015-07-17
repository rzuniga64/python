"""
     Purpose: A reusable GUI module that contains a Label and Entry.
     Input: text to be displayed in the Label
"""
from tkinter import *


class LabelEntry(Frame):                # an extended Frame
    def __init__(self, parent=None, **config):
        Frame.__init__(self, parent)    # do superclass init
        self.pack()
        # Create and pack the widgets for frame
        self.label1 = Label(parent, **config).pack(padx=5, pady=5, side=LEFT, expand=YES, fill=BOTH)
        self.entry1 = Entry(parent, justify=LEFT)
        self.entry1.pack(padx=5, pady=5, side=LEFT, expand=YES, fill=BOTH)

    def get_entry(self):
        return self.entry1.get()

if __name__ == '__main__':
    root = Tk()
    LabelEntry(root, text='First Name')
    root.mainloop()