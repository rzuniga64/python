from tkinter import *                   # get Tk widget classes
from time import sleep
import _thread
from LabelEntry import LabelEntry       # get the LabelEntry class
from StudentDB import StudentDB         # get the StudentDB class

    # Purpose: to allow a user to input student information and from
    # a GUI interface.  The user will press a button to add input
    # data into a database.  The user will press a button to
    # retrieve all data input into database.
    # Input: A list of values input from a GUI interface


class StudentContainer():
    def __init__(self):

        # Create a database to store information typed into the GUI interface
        self.studentdb = StudentDB()
        self.le0, self.le1, self.le2, self.le3, self.le4 = '', '', '', '', ''
        self.le5, self.le6, self.le7, self.le8, self.le9 = '', '', '', '', ''

        # Create the main window
        self.root = Tk()
        self.root.title("Enter Student Information")
        self.message = StringVar()
        self.text = ' '

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

        # Start the main loop.
        self.root.mainloop()

    def make_widgets(self):
        # Labels and Edit boxes
        self.le0 = LabelEntry(self.frame1, text="First Name", width=14, anchor=E)
        self.le0.pack(padx=5, pady=5, side=RIGHT)
        self.le1 = LabelEntry(self.frame1, text="Last Name", width=14, anchor=E)
        self.le1.pack(padx=5, pady=5, side=RIGHT)
        self.le2 = LabelEntry(self.frame2, text="Street", width=14, anchor=E)
        self.le2.pack(padx=5, pady=5, side=RIGHT)
        self.le3 = LabelEntry(self.frame2, text="City", width=14, anchor=E)
        self.le3.pack(padx=5, pady=5, side=RIGHT)
        self.le4 = LabelEntry(self.frame3, text="State", width=14, anchor=E)
        self.le4.pack(padx=5, pady=5, side=RIGHT)
        self.le5 = LabelEntry(self.frame3, text="Zip", width=14, anchor=E)
        self.le5.pack(padx=5, pady=5, side=RIGHT)
        self.le6 = LabelEntry(self.frame4, text="Email", width=14, anchor=E)
        self.le6.pack(padx=5, pady=5, side=RIGHT)
        self.le7 = LabelEntry(self.frame4, text="Phone", width=14, anchor=E)
        self.le7.pack(padx=5, pady=5, side=RIGHT)
        self.le8 = LabelEntry(self.frame5, text="School", width=14, anchor=E)
        self.le8.pack(padx=5, pady=5, side=RIGHT)
        self.le9 = LabelEntry(self.frame5, text="Major", width=14, anchor=E)
        self.le9.pack(padx=5, pady=5, side=RIGHT)

        # Add button and label
        add_button = Button(self.frame6, text="Add to database", command=self.on_click_add)
        add_button.config(relief=RAISED, bg="light blue", fg="black")
        add_button.pack(padx=5, pady=5, side=LEFT)
        Label(self.frame6, textvariable=self.message).pack(side=LEFT)

        # Text box and scrollbar
        sbar = Scrollbar(self.frame7)
        text = Text(self.frame7, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set, bd=5, height=15, width=130)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

        # Display, Clear and Quit buttons
        display_button = Button(self.frame8, text="Display students", command=self.on_click_display)
        display_button.config(relief=RAISED, bg="light blue", fg="black")
        display_button.pack(padx=5, pady=5, side=LEFT)
        clear_button = Button(self.frame8, text="Clear", command=self.clear_text)
        clear_button.config(relief=RAISED, bg="light blue", fg="black")
        clear_button.pack(padx=5, pady=5, side=LEFT)
        quit_button = Button(self.frame8, text="Quit", command=exit)
        quit_button.config(relief=RAISED, bg="light blue", fg="black")
        quit_button.pack(padx=5, pady=5, side=LEFT)

    def set_text(self, text=' '):
        self.text.delete('1.0', END)                     # delete current text from text box
        self.text.insert('1.0', text)                    # add at line 1, col 0
        self.text.mark_set(INSERT, '1.0')                # set insert cursor
        self.text.focus()                                # save user a click

    def clear_message(self, count):                        # function run in threads
        for i in range(count):
            sleep(count)                            # simulate real work
            self.message.set(' ')

    def on_click_add(self):
        fname = self.le0.get_entry()
        lname = self.le1.get_entry()
        street = self.le2.get_entry()
        city = self.le3.get_entry()
        state = self.le4.get_entry()
        zipcode = int(self.le5.get_entry())
        email = self.le6.get_entry()
        phone = self.le7.get_entry()
        school = self.le8.get_entry()
        major = self.le9.get_entry()
        student_info = [fname, lname, street, city, state, zipcode, email, phone, school, major]
        is_inserted = self.studentdb.insert_record(student_info)
        if is_inserted:
            self.message.set('Student successfully added!')
            for i in range(5):
                _thread.start_new_thread(self.clear_message, (5,))     # each thread loops 5 times

    def on_click_display(self):
        text = ' '
        student_table = self.studentdb.run_query('select * from student')
        for record in student_table:
            for attribute in record:
                text += str(attribute)+' '
            text += '\n'
        self.set_text(text)
        print()

    def clear_text(self):
        self.text.delete('1.0', END)                     # delete current text from text box

test_gui = StudentContainer()
