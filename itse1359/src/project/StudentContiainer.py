from tkinter import *                   # get Tk widget classes
from LabelEntry import LabelEntry       # get the LabelEntry class


class StudentContainer():
    def __init__(self, text=' '):
        # Create the main window
        self.root = Tk()
        self.root.title("Enter Student Information")
        self.message = StringVar()

        # Create frames
        self.frame1 = Frame(self.root)
        self.frame2 = Frame(self.root)
        self.frame3 = Frame(self.root)
        self.frame4 = Frame(self.root)
        self.frame5 = Frame(self.root)
        self.frame6 = Frame(self.root)
        self.frame7 = Frame(self.root)
        self.frame8 = Frame(self.root)

        # Pack the frames
        self.frame1.pack(expand=YES, fill=BOTH)
        self.frame2.pack(expand=YES, fill=BOTH)
        self.frame3.pack(expand=YES, fill=BOTH)
        self.frame4.pack(expand=YES, fill=BOTH)
        self.frame5.pack(expand=YES, fill=BOTH)
        self.frame6.pack(expand=YES, fill=BOTH)
        self.frame7.pack(expand=YES, fill=BOTH)
        self.frame8.pack(expand=YES, fill=BOTH)

        self.make_widgets()
        self.set_text(text)

        # Start the main loop.
        self.root.mainloop()

    def on_click_add(self):
        self.message.set('Student successfully added!')

    def make_widgets(self):
        # Create and pack the widgets for frame 1
        LabelEntry(self.frame1, text="First Name", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame1, text="Last Name", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame2, text="Street", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame2, text="City", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame3, text="State", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame3, text="Zip", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame4, text="Email", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame4, text="Phone", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame5, text="School", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        LabelEntry(self.frame5, text="Major", width=14, anchor=E).pack(padx=5, pady=5, side=RIGHT)
        Button(self.frame6, text="Add", command=self.on_click_add, relief=RAISED, bg="light blue", fg="black").pack(padx=75,pady=5, side=LEFT)
        Label(self.frame6, textvariable=self.message).pack(side=LEFT)
        sbar = Scrollbar(self.frame7)
        text = Text(self.frame7, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set, bd=5, height=15)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text
        Button(self.frame8, text="Display List of Students", command=self.on_click_add, relief=RAISED, bg="light blue", fg="black").pack(padx=5 ,pady=5, side=LEFT)
        Button(self.frame8, text="Clear", command=self.clear_text, relief=RAISED, bg="light blue", fg="black").pack(padx=5 ,pady=5, side=LEFT)
        Button(self.frame8, text="Quit", command=exit, relief=RAISED, bg="light blue", fg="black").pack(padx=5 ,pady=5, side=LEFT)

    def set_text(self, text=' '):
        self.text.delete('1.0', END)                     # delete current text
        self.text.insert('1.0', text)                    # add at line 1, col 0
        self.text.mark_set(INSERT, '1.0')                # set insert cursor
        self.text.focus()                                # save user a click

    def clear_text(self):
        self.text.delete('1.0', END)                     # delete current text

test_gui = StudentContainer(text='Words\ngo here')