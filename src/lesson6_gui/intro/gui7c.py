import gui7
from tkinter import *


class HelloPackage(gui7.HelloPackage):
    """
    The class could make this better by defining a method
    that always routes unknown attribute fetches to the
    embedded frame.   This script extends HelloPackage from
    gui7c.
    """
    def __getattr__(self, name):
        return getattr(self.top, name)                  # pass off to a real widget

if __name__ == '__main__':
    HelloPackage().mainloop()    # invokes __getattr__
