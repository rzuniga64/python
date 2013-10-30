from tkinter import *

root = Tk()

widget = Label(root, text="Eat at Joe's")   # setting label text
# setting the background, foreqround, cursor, and font
widget.config(bg='black', fg='red', cursor='cross', font=('Times', 24, 'italic'))
widget.pack(expand=YES, fill=BOTH)
root.mainloop()