import tkinter as tk
import random

def generate_random():
    
    randomomizer = random.randint(100000000000, 1000000000000000000)
    label.config(text=f"Random Number: {randomomizer}")

root = tk.Tk()
label = tk.Label(root, text="Generate Random password", font=("Sans comic", 14))
label.pack(pady=40)

button = tk.Button(root, text="Press to generate passcode", command=generate_random, font=("Sans comic", 14))
button.pack(pady=35)

root.mainloop()