from tkinter import *
from tkinter import messagebox


def on_click():
    global evar
    print("you clicked me: ", evar.get())
    # display a simple message box with two buttons - Yes and No
    result = messagebox.askyesno(message="you entered: " + evar.get(), icon='warning', title='What you entered')
    # return will be either True or False, depending
    # on which button is clicked by the user.
    if result:
        print("on_click: you clicked Yes")
    else:
        print("on_click: you clicked No")

root = Tk()

evar = StringVar()
widget1 = Entry(root, textvariable=evar)
widget1.pack(padx=5, pady=5, side=TOP)

widget2 = Button(root, text="Click Me", command=on_click, bg="light blue", fg="red")
widget2.pack(padx=5, pady=5, side=TOP)

root.mainloop()