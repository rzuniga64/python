from tkinter import *

state = ''
buttons = []


def choose(j):
    global state
    state = j
    for btn in buttons:
        btn.deselect()
    buttons[j].select()

root = Tk()

for i in range(4):
    radio = Radiobutton(root, text=str(i), value=str(i), command=(lambda i=i: choose(i)))
    radio.pack(side=BOTTOM)
    buttons.append(radio)

root.mainloop()
print("You chose the following number: ", state)