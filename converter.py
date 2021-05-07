"""
Metric Unit Converter
3/27/2019
Using Tkinter GUI Library (For Developing Native Windows Applications)

Component of the Chemistry Companion Application,
Converts Metric & Imperial to Metric Units of Length
"""

from tkinter import *

root = Tk()

root.title("Metric Unit Converter")


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def get_conversion(value, from_unit, to_unit):
    converted_num = 0.0

    imperial_to_meters = {
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }

    meters_to_metric = {
        "mm": 1000.0,
        "cm": 100.0,
        "m": 1.0,
        "hm": 0.01,
        "km": 0.001
    }

    # If imperial, convert to metric
    if from_unit in imperial_to_meters.keys():
        num_meters = value * imperial_to_meters[from_unit]
        converted_num = num_meters * meters_to_metric[to_unit]
    else:
        converted_num = (value / meters_to_metric[from_unit]) * meters_to_metric[to_unit]

    return converted_num

def convert(*args):
    user_num = float(entry_box.get())

    from_unit = from_menu_string.get()
    to_unit = to_menu_string.get()

    c_num = get_conversion(user_num, from_unit, to_unit)
    c_num = "{:,}".format(c_num)

    converted_num.config(text=c_num, font="Helvetica 35 bold underline")


center_window(750, 575)

from_units = {'mi', 'yd', 'ft', 'in', 'km', 'hm', 'm', 'cm', 'mm'}
to_units = {'km', 'hm', 'm', 'cm', 'mm'}

from_menu_string = StringVar(root)
to_menu_string = StringVar(root)

from_menu_string.set('m')
to_menu_string.set('m')

title = Label(text="Metric Unit Converter", font="Helvetica 35 bold", pady=15)

from_menu = OptionMenu(root, from_menu_string, *from_units)
from_menu.configure(font=('Helvetica', 20))

entry_box = Entry(root, font="Helvetica 20", justify="center")
equals_label = Label(text="=", font="Helvetica 100 bold")
submit_button = Button(root, text="Convert", command=convert, font="Helvetica 20 bold")

to_menu = OptionMenu(root, to_menu_string, *to_units)
to_menu.configure(font=('Helvetica', 20))

converted_num = Label(root, text="________", font="Helvetica 35 bold")



title.pack()


entry_box.bind("<Return>", convert)
entry_box.pack(pady=10)
from_menu.pack()
equals_label.pack()

converted_num.pack()

to_menu.pack()
submit_button.pack(pady=25)

root.mainloop()
