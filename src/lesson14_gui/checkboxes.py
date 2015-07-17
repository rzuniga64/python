from tkinter import *

states = []


def check(j):
    states[j] = not states[j]

root = Tk()
for i in range(4):
    test = Checkbutton(root, text=str(i), command=(lambda j=i: check(j)))
    test.pack(side=TOP)
    states.append(0)

root.mainloop()
print(states)