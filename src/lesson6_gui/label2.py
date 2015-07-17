from tkinter import *

root = Tk()

frame1 = Frame(root)
frame1.pack()

widget1 = Label(frame1, text="Hi there", bg="red")
widget1.pack(padx=5, pady=5, side=TOP)

widget2 = Label(frame1, text="Hi there 2", bg="yellow")
widget2.pack(padx=5, pady=5, side=TOP)
#############################################################

frame2 = Frame(root)
frame2.pack()

widget3 = Label(frame2, text="Hi there", bg="green")
widget3.pack(padx=5, pady=5, side=LEFT)

widget4 = Label(frame2, text="Hi there 2", bg="#D09712")
widget4.pack(padx=5, pady=5, side=RIGHT)

root.mainloop()