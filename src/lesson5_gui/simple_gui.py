"""
Purpose: create a simple GUI

Create an interface with the following widgets and functionality.

Each widget should have a padding of 5 pixels in each dimension (x and y).

1. Label 1 with the text "Number 1:", anchored to the top.
2. Entry 1 to the right of label 1.
3. Label 2 with the text "Number 2:", below label 1.
4. Entry 2 to the right of label 2.
5. Button with the text "Add", below label 2. This button should call a function that gets the values from entry 1
   and entry 2, adds them and prints out the total.

(Hint: you'll want to use a Frame for label 1/entry 1 and label 2/entry 2)
"""

from tkinter import *


class SimpleGUI:
    def __init__(self):
        #Create the main window
        self.root = Tk()

        # Create 3 frames
        self.frame1 = Frame(self.root)
        self.frame2 = Frame(self.root)
        self.sum_frame = Frame(self.root)
        self.button_frame = Frame(self.root)
        
        # Pack the frames
        self.frame1.pack()
        self.frame2.pack()
        self.sum_frame.pack()
        self.button_frame.pack()
        
        # Create and pack the widgets for frame 1
        self.label1 = Label(self.frame1, text='Number 1')
        self.entry1 = Entry(self.frame1, width=10)
        self.label1.pack(padx=5, pady=5, side='left')
        self.entry1.pack(padx=5, pady=5, side='left')
        
        #Create and pack the widgets for frame2
        self.label2 = Label(self.frame1, text='Number 2')
        self.entry2 = Entry(self.frame1, width=10)
        self.label2.pack(padx=5, pady=5, side='left')
        self.entry2.pack(padx=5, pady=5, side='left')
        
        # Create and pack the widgets for sum_frame
        self.label3 = Label(self.sum_frame, text='Total')
        self.sum = StringVar()  # to update sum_label
        self.sum_label = Label(self.sum_frame, textvariable=self.sum)
        self.label3.pack(padx=5, pady=5, side='left')
        self.sum_label.pack(padx=5, pady=5, side='left')
        
        # Create and pack the widgets for button_frame
        self.add_button = Button(self.button_frame, text='Add', command=self.add)
        self.quit_button = Button(self.button_frame, text='Quit', command=self.root.destroy)
        
        self.add_button.pack(padx=5, pady=5, side='left')
        self.quit_button.pack(padx=5, pady=5, side='left')
        
        # Start the main loop.
        self.root.mainloop()
        
    def add(self):
        # Get the two numbers and store them in variables
        self.num1 = float(self.entry1.get())
        self.num2 = float(self.entry2.get())
        
        # Calculate the sum

        self.sum_of_nums = self.num1 + self.num2
        self.sum.set(self.sum_of_nums)
            
test_gui = SimpleGUI()