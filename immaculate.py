# !/usr/bin/python3
import sys
from action.Films import *
from tkinter import *
from tkinter import messagebox


def films():

    inputString = e.get();

    if len(inputString) > 0:
        film = Films(e.get(), 400000000)
        output = film.moveFiles()
        messagebox.showinfo("Immaculate", output)
    else:
        messagebox.showinfo("Immaculate", "No Directory Given")


top = Tk()
top.wm_title("Immaculate")
top.geometry("200x100")
top.wm

b = Button(top, text="Run", command=films)
b.pack(side=RIGHT)

L1 = Label(top, text="Directory:")
L1.pack(side=LEFT)

e = Entry(top)
e.pack(side=RIGHT)

top.mainloop()
