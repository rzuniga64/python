from tkinter import *


class HelloPackage:                            # not a widget subclass
    """
    This class serves as a generator of namespaces for storing away real
    widget objects and state.  Because of that, widgets are attached to self.top
    (an embedded Frame), not to self. All references to the object as a widget
    must descend to the embedded frame, as in the top.mainloop call to start
    the GUI at the end of the script.
    """
    def __init__(self, parent=None):
        self.top = Frame(parent)               # embed a Frame
        self.top.pack()
        self.data = 0
        self.make_widgets()                    # attach widgets to self.top

    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)

    def message(self):
        self.data += 1
        print('Hello number', self.data)

    # define a method that always routes unknown attribute fetches to the embedded frame.
    def __getattr__(self, name):
        return getattr(self.top, name)                  # pass off to a real widget

if __name__ == '__main__':
    HelloPackage().top.mainloop()
