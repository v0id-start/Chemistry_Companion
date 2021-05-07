"""
Periodic Table of Elements
3/27/2019
Using Tkinter GUI Library (For Developing Native Windows Applications)

Component of the Chemistry Companion Application,
Opens a window that displays the Periodic Table of Elements

opens pte.png
"""

from tkinter import *
from PIL import ImageTk, Image

root=Tk()

image = Image.open('pte.png')
# The (450, 350) is (height, width)
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image=my_img)
my_img.pack()

root.mainloop()
