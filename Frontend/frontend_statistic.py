"""
    Laborprojekt IngInfo III
    Produktivcode Frontend - Statistikseite
"""

### IMPORTS & VARIABLEN
import frontend_home as fh
import tkinter as tk
import tkinter.font as tkFont

### Funktionen
def b_home_click():
    newwin.destroy()                           # destroy um Fenster zu vernichten
    fh

### START
newwin = tk.Toplevel()                  # Toplevel, weil keine 2 Hauptfenster möglich!
newwin.title("Projekt - Labor Ingenieurinformatik 3")
width = 600
height = 500
screenwidth = newwin.winfo_screenwidth()
screenheight = newwin.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
newwin.geometry(alignstr)
newwin.resizable(width=False, height=False)

label = tk.Label(
    newwin,
    bg="#dddddd",
    font=tkFont.Font(family='Times', size=10),
    fg="#000000",
    justify="center",
    text="",
)
label.place(x=10, y=10, width=120, height=25)

b_home = tk.Button(
    newwin,
    bg="#dddddd",
    font=tkFont.Font(family='Times', size=10),
    fg="#000000",
    justify="center",
    text="Home",
    command=b_home_click
)
b_home.place(x=510, y=10, width=70, height=25)

newwin.mainloop()