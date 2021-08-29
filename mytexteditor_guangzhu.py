"""
[Final Quiz]
Date: 2021-08-23
Design at least 3 major features for a text editor
Do a quick research on the Internet if you need some ideas or references
Save your project as 'mytexteditor'
Share your project to github
Post your URL of your remote git repository to SLACK
Due date: 2021-08-31
Hints:
Self-study on font family, size, weight of text widget in Tkinter
"""
# imports
from tkinter import *
from tkinter.ttk import Separator
from tkinter import font


# functions
def font_helvetica():
    global family
    family = 'Helvetica'
    settings.config(family=family)


def font_calibri():
    global family
    family = 'Calibri'
    settings.config(family=family)


def font_times_new_roman():
    global family
    family = 'Times New Roman'
    settings.config(family=family)


def font_courier_new():
    global family
    family = 'Courier New'
    settings.config(family=family)


def font_verdana():
    global family
    family = 'Verdana'
    settings.config(family=family)


def size_8():
    global size
    size = 8
    settings.config(size=size)


def size_12():
    global size
    size = 12
    settings.config(size=size)


def size_16():
    global size
    size = 16
    settings.config(size=size)


def size_24():
    global size
    size = 24
    settings.config(size=size)


def size_36():
    global size
    size = 36
    settings.config(size=size)


def size_72():
    global size
    size = 72
    settings.config(size=size)


def weight_normal():
    global weight
    weight = 'normal'
    settings.config(weight=weight)


def weight_bold():
    global weight
    weight = 'bold'
    settings.config(weight=weight)


# main window
root = Tk()
root.title("My Text Editor | guangzhu")
root.geometry("640x480+300+300")

# default fonts
family = 'Helvetica'
size = 12
weight = 'normal'
settings = font.Font(family=family, size=size, weight=weight)
# menubar
menu_bar = Menu(root)
family_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Font Family ▼", menu=family_menu)

family_menu.add_command(label='Helvetica', command=font_helvetica)
family_menu.add_command(label='Calibri', command=font_calibri)
family_menu.add_command(label='Times New Roman', command=font_times_new_roman)
family_menu.add_command(label='Courier New', command=font_courier_new)
family_menu.add_command(label='Verdana', command=font_verdana)

size_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Font size ▼", menu=size_menu)

size_menu.add_command(label='8', command=size_8)
size_menu.add_command(label='12', command=size_12)
size_menu.add_command(label='16', command=size_16)
size_menu.add_command(label='24', command=size_24)
size_menu.add_command(label='36', command=size_36)
size_menu.add_command(label='72', command=size_72)

weight_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Font weight ▼", menu=weight_menu)

weight_menu.add_command(label='Normal', command=weight_normal)
weight_menu.add_command(label='Bold', command=weight_bold)

# text frame
frame_text = Frame(root, height=30)
frame_text.pack(anchor=CENTER, fill=BOTH, expand=Y)

# text widget
text = Text(frame_text, height=5, width=30)
text.config(font=settings)
text.pack(side=LEFT, fill=BOTH, expand=Y)

# scrollbar
scrollbar = Scrollbar(frame_text)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

# textarea frame
frame_status = Frame(root)
frame_status.pack(anchor=CENTER, fill=X)

# separator
sep = Separator(frame_status, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# mainloop
root.config(menu=menu_bar)
root.mainloop()
