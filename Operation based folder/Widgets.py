# from tkinter import Tk
# from PIL import Image, ImageTk

# import os

# print("Current Working Directory:", os.getcwd())
# root= Tk()
# root.geometry("400x400")

# upload = Image.open("C:\Users\hp\OneDrive\Desktop\Python Codingal\Conditional Statement\Operation based folder\Random.png")
# image = ImageTk.PhotoImage(upload)

# label1 = Label(root , image=image , height="2234px" , length="230px")
# label1.place(x=25 , y=55)
# label2 = Label(root,text="This is how you print images using Tkinter")
# label2.place(x=45 , y=65)

# root.mainloop()

from tkinter import *

from PIL import Image, ImageTk

import os

# Set the working directory to the script's directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Debugging: Print the current working directory

print("Current Working Directory:", os.getcwd())

# Create a window with a title bar and set its geometry as well

root = Tk()

root.title('image')

root.geometry('600x800')

# Try to open the image file

try:

# Provide the correct path to the image file (using raw string)

    image_path = r"C:\Users\hp\OneDrive\Desktop\Python Codingal\Conditional Statement\Operation based folder\Random.png"

    upload = Image.open(image_path)

    print("Image opened successfully!")

except FileNotFoundError:

    print(f"Error: The file '{image_path}' was not found. Please check the path.")

except Exception as e:

    print(f"An error occurred while opening the image: {e}")

# Convert this Image to Tkinter compatible image

image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label

label = Label(root, image=image, height=350, width=300)

label.place(x=50, y=0)

label2 = Label(root, text="This is how you add image in Tkinter Window")

label2.place(x=40, y=360)

# Run the application

root.mainloop()