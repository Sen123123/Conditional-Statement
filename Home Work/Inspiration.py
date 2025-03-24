# Had to check tutorial for random number generation
import tkinter as T
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, T.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = T.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

length_label = T.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = T.Entry(root)
length_entry.pack(pady=5)

generate_button = T.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = T.Entry(root, width=50)
password_entry.pack(pady=5)

root.mainloop()
