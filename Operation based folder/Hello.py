from tkinter import *
from tkinter import Tk

window= Tk()
window.title("Sample Window")
window.geometry("300x300")

greeting= Label(text="Hello user", fg= "black",bg= "white")
button = Button(text="Click me", bg= "black", fg= "white")
entry = Entry(fg= "yellow", bg= "orange", width = 50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master= window, relief= RAISED, borderwidth=5)
frame.pack()
label = Label(master = frame, text="sample text")
label.pack()

Textbox = Text(fg="green", bg="yellow")
window.mainloop()