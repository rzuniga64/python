from tkinter import *


def result():
    print('the sum of 2+2 is ", 2+2')

win = Frame()
win.pack()

Button(win, text='Add', command=result).pack(side=LEFT)
Label(win, text='Click Add to get the sum or Quite to Exit').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
win.mainloop()