#import matplotlib as plt
######################################################
"""
    Laborprojekt IngInfo 3
    Produktivcode Frontend - Startseite
"""


### IMPORTS & VARIABLEN
import frontend_statistic as fs
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkcalendar import Calendar


first =  True

### FUNKTIONEN
def b_statistic_click():
    root.destroy()
    fs

### START
if (first == True):
    first = False
    root = tk.Tk()
    root.title("Projekt - Labor Ingenieurinformatik 3")
    width=600
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

bauteil = ("Bauteil auswählen", "Doppel-T-Träger", "T-Träger", "L-Träger", "Vollwelle")
var = tk.Variable(value=bauteil)
var.set(bauteil[0])

### NAVIGATION
b_statistic = tk.Button(
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "center",
    text = "Statistic",
    command = b_statistic_click
)
b_statistic.place(x=510, y=10, width=70, height=25)

lab =tk.Label(text="")
lab.place(x=10, y=50, width=150, height=25)

### BAUTEILAUSWAHL
opt = tk.OptionMenu(root, var, *bauteil)             # Dropdownliste erstellen, *bauteil: alle Elemente aus Liste
opt.config(width=90, font=('Helvetica', 10))
opt.place(x=10, y=10, width=150, height=25)

def callback(*args):
    lab["text"] = var.get()          # var.get(): in Dropdownmenü ausgewählter Wert
    return

var.trace("w", callback)        # nutzt callback-Fkt, um Varaiblenwert zu bekommen


"""
### AUSWAHL ZEITRAUM
def get_date():
    date.config(text="Selected Date is:" + cal.get_date())

cal = Calendar(
    selectmode = "day",
    year = 2022,
    month = 5,
    day = 22
)
cal.place(x=130, y=80)

b_startdatum = tk.Button(
    root,
    bg="#dddddd",
    font=tkFont.Font(family='Times', size=10),
    fg="#000000",
    justify="center",
    text="Get Date",
    command=get_date
)
b_startdatum.place(x=10, y=80, width=70, height=25)

startdatum = tk.Label(root, text = "")
startdatum.place(x=10, y=80, width=70, height=25)
"""

root.mainloop()
