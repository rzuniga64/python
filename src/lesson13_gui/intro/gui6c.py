from tkinter import *                    # get Tk widget classes
from gui6 import Hello                   # get the subframe class


class HelloContainer(Frame):
    """
    A specialized Frame but it attaches an instance of the original
    Hello class in a more object-oriented fashion. This class registers
    the added button's callback handler as self.quit, which is just
    the standard quit widget method this class inherits from Frame.
    The window this time represents two Python classes at work - the
    embedded component's widgets on the right(the original Hello button)
    and the container's widgets on the left.
    """
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        Hello(self).pack(side=RIGHT)     # attach a Hello to me
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    HelloContainer().mainloop()
