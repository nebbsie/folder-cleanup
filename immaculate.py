# !/usr/bin/python3
import sys
from action.Films import *
from tkinter import *


def films():
    film = Films(e.get(), 400000000).moveFiles()


top = Tk()
top.wm_title("Immaculate")
top.geometry("200x100")

b = Button(top, text="Run", command=films)
b.pack(side=RIGHT)

L1 = Label(top, text="Directory:")
L1.pack(side=LEFT)

e = Entry(top)
e.pack(side=RIGHT)

top.mainloop()
