from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Division")
root.configure(bg="light blue")
root.geometry('450x650')
upload = Image ('random image *****')

upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image= image , bg='orange')
label = Place(x=56, y=23)

label1= Label(root, text='HELLO USER TYPE SOMETHING!',bg='green')

Label.place(relx=0.5, y=340 anchor=CENTER)
            
def msg() :
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want the calculation to be denominated?")              
    if MsgBox == 'ok':
        topwin() 

button1 = Button(root, text = "", command=msg,bg='brown', fg='white')
button1.place(x=260, y=125)

top= Toplevel()
top.title