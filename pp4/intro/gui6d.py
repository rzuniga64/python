from tkinter import *
from gui6 import Hello


class HelloExtender(Hello):
    """
    To extend Hello instead of just attaching to it, we just override
    some of its methods in a new subclass(which itself becomes a
    specialized Frame widget).

    This example demonstrates a that to change a GUI's behaviour, we can
    write a new class that customizes its parts rather than changing the
    existing GUI code in place.  The main code need be debugged only once
    and can be customized with subclasses as unique needs arise.
    """
    def make_widgets(self):                       # extend method here
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)                 # redefine method here

if __name__ == '__main__':
    HelloExtender().mainloop()
