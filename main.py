"""
Chemistry Companion
3/27/2019
Using Tkinter GUI Library (For Developing Native Windows Applications)

Main file launches on startup, displays menu layout with buttons
to different functions.

opens:
-compound_namer.py
-converter.py
-pte.py
"""

#Using functions from the Tkinter, OS, Subprocess, and Random libraries
from tkinter import *
import tkinter.messagebox
import os
import random
import subprocess

root = Tk()
root.title("Chemistry Companion")

chem_jokes = ["I'd tell you a chemistry joke but Na", "Have you heard the one about a chemist who was reading a book about helium?\n\nHe just couldn't put it down.", "What did Helium say to his friend Droxide?\n\n Hi, Droxide!", "I asked the guy sitting next to me if he had any Sodium Hypobromite…\n\nHe said NaBrO", "What is the show cesium and iodine love watching together?\n\nCSI", "We would like to apologize for not adding more jokes... but we only update them.... periodically!", "Making bad chemistry jokes because all the good ones Argon", "Helium walks into a bar, The bar tender says\n'We don't serve noble gasses in here.'\nHelium doesn't react.", "Silver walks up to Gold in a bar and says, 'AU, get outta here!'", "Two chemists go into a restaurant.\nThe first one says 'I think I'll have an H2O.'\nThe second one says 'I think I'll have an H2O too' -- and he died.", "What did the scientist say when he found 2 isotopes of helium?\n\nHeHe", "Why was the mole of oxygen molecules excited when he walked out of the singles bar?\n\nHe got Avogadro's number!", "A proton and a neutron are walking down the street.\nThe proton says, 'Wait, I dropped an electron help me look for it.'\nThe neutron says 'Are you sure?' The proton replies 'I'm positive.'", "The optimist sees the glass half full.\nThe pessimist sees the glass half empty.\nThe chemist see the glass completely full, half in the liquid state and half in the vapor state.", "When one physicist asks another, 'What's new?' what's the typical response?\n\nC over lambda.", "What kind of fish is made out of 2 sodium atoms?\n\n2 Na"]

"""
The following function: "center_window" is
provided by Ene Uran from:

https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
"""
######################################
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
########################################


#Links to open subprocesses from buttons
def open_compound_namer():
    subprocess.Popen(['python', 'compound_namer.py'])

def open_pte():
    subprocess.Popen(['python', 'pte.py'])

def open_converter():
    subprocess.Popen(['python', 'converter.py'])

def display_joke():
    random_joke = random.choice(chem_jokes)
    tkinter.messagebox.showinfo("CHEM JOKESTER 2000", random_joke)

def quit_app():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to exit Chemistry Companion?"):
        root.destroy()


#Creates menu layout with buttons assigned functions
def main():
    top_frame = Frame(root)
    top_frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    main_frame = Frame(root)
    main_frame.pack()


    #CREATE MENU ELEMENTS
    title_label = Label(top_frame, text="CHEMISTRY COMPANION", font="Helvetica 35 bold")

    equation_button = Button(top_frame, text="Determine a Compound", pady=10, padx=20, command=open_compound_namer, bg="lightblue", font="Helvetica 14 bold italic")
    formulas_button = Button(top_frame, text="Metric Unit Converter", pady=10, padx=30, command=open_converter, bg="lightblue", font="Helvetica 14 bold italic")
    pte_button = Button(top_frame, text="Periodic Table of Elements", pady=10, padx=5, command=open_pte, bg="lightblue", font="Helvetica 14 bold italic")
    joke_button = Button(top_frame, text="Tell Me a Chemistry Joke", pady=10, padx=15, command=display_joke, bg="lightblue", font="Helvetica 14 bold italic")
    exit_button = Button(top_frame, text="EXIT", pady=5, padx=5, bg="red", fg="white", font="Helvetica 14 bold", command=quit_app)



    #DISPLAY MENU
    title_label.pack(pady=25)

    equation_button.pack(pady=22)
    formulas_button.pack(pady=22)
    pte_button.pack(pady=22)
    joke_button.pack(pady=22)
    exit_button.pack(pady=30)


center_window(650, 650)

if __name__ == "__main__":
    main()


root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
