"""
Compound Namer
3/27/2019
Using Tkinter GUI Library (For Developing Native Windows Applications)

Component of the Chemistry Companion Application,
Names compounds given the formula and vice versa

opens compounds.txt
"""

from tkinter import *

file = open("compounds.txt", "r")
line_count = len(file.readlines())
file.seek(0)

root = Tk()
root.title("Compound Determiner")

"""
The following function: "center_window" is
provided by Ene Uran from:

https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
"""
###############################################
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
##############################################


def get_input(*args):
    found = False
    compound = ""
    file.seek(0)
    user_compound = entry_box.get()

    for line_num in range(1, line_count + 1):
        compound_info = file.readline().strip().split()

        if len(compound_info) >= 2:


            #USER ENTERS COMPOUND FORMULA
            if user_compound == compound_info[0]:
                for info in compound_info:
                    if info.isalpha():
                        compound = compound + " " + info
                        compound_label.config(text=compound.upper(), fg="blue")
                        found = True

            #USER ENTERS COMPOUND NAME
            elif (user_compound in " ".join(compound_info)) and (user_compound.islower()) and (all(x.isalpha() or x.isspace() for x in user_compound)):
                compound = compound_info[0]
                compound_label.config(text=compound, fg="blue")
                found = True

    if not found:
        compound_label.config(text="Compound Not Found", fg="red")
    entry_box.delete(0, 'end')


center_window(650, 400)

title = Label(root, text="Compound Determiner", font="Helvetica 40 bold")
description = Label(root, text="Enter a Compound's Name or Formula", pady=15, font=("Helvetica", 17))
example = Label(root, text="Ex: 'H2O' or 'water'", font="Helvetica 16 italic", pady=15)
entry_box = Entry(root, font="Helvetica 30", justify='center')
submit_button = Button(root, text="Submit", command=get_input, font="Helvetica 13 bold")
compound_label = Label(root, text="COMPOUND", font="Helvetica 35 bold", pady=20)

title.pack()
description.pack()
example.pack()

entry_box.bind("<Return>", get_input)
entry_box.pack()

submit_button.pack(pady=20)
compound_label.pack()


root.mainloop()
