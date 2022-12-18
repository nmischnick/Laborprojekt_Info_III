"""
    Laborprojekt IngInfo 3
    Produktivcode Frontend - Startseite
"""


### IMPORTS & VARIABLEN
import frontend_statistic as fs
import tkinter as tk
import tkinter.font as tkFont


### FUNKTIONEN
def b_statistic_click():
    root.quit()                                 # quit um Fenster im Hintergrund zu halten
    fs

def datum_uebernehmen():
    start_ges.configure(state='normal')                # Textwidget nicht mehr schreibgeschützt
    end_ges.configure(state='normal')
    start_ges.delete("1.0", "end")                     # Textfeld leeren
    end_ges.delete("1.0", "end")
    text_start_ges = ("Ausgewähltes Startdatum:\n {}".format(e1_startdatum.get() + " " + e2_startdatum.get()))
    start_ges.insert(tk.END, text_start_ges)
    start_ges.configure(state='disabled')       # Textwidget schreibgeschützt machen
    text_ende_ges = ("Ausgewähltes Enddatum:\n {}".format(e3_enddatum.get() + " " + e4_enddatum.get()))
    end_ges.insert(tk.END, text_ende_ges)
    end_ges.configure(state='disabled')


"""
### VERBINDUNG ZUR DATENBANK
def connection(db):
    pymysql.connect(host="abc", user="def", password="", db=db)

db = "test"
connection(db)
"""

### START
root = tk.Tk()
root.title("Projekt - Labor Ingenieurinformatik 3")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

bauteil = ("Doppel-T-Träger", "T-Träger", "L-Träger", "Vollwelle")      # aus Datenbank abfragen!
var = tk.Variable(value=bauteil)
var.set("Bauteil auswählen")

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

### AUSWAHL START- & ENDDATUM
start_ges = tk.Text(
        bg="#dddddd",
        font=tkFont.Font(family='Times', size=10),
        fg="#000000"
    )
start_ges.place(x=320, y=40, width=180, height=70)

end_ges = tk.Text(
    bg="#dddddd",
        font=tkFont.Font(family='Times', size=10),
        fg="#000000"
)
end_ges.place(x=320, y=120, width=180, height=70)

startdatum1 = tk.Text(
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000"
)
text_startdatum1 = "Startdatum eingeben \nDD.MM.YYYY"
startdatum1.insert(tk.END, text_startdatum1)        # Beschriftung in Textfeld einfügen
startdatum1.configure(state='disabled')
startdatum1.place(x=10, y=40, width=150, height=50)

startdatum2 = tk.Text(
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000"
)
text_startdatum2 = "\nHH:MM"
startdatum2.insert(tk.END, text_startdatum2)        # Beschriftung in Textfeld einfügen
startdatum2.configure(state='disable')
startdatum2.place(x=160, y=40, width=150, height=50)


e1_startdatum = tk.Entry(                           # Eingabe Startdatum (Datum)
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "left"
)
e1_startdatum.place(x=10, y=80, width=150, height=25)

e2_startdatum = tk.Entry(                           # Eingabe Startdatum (Uhrzeit)
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "left"
)
e2_startdatum.place(x=160, y=80, width=150, height=25)

enddatum1 = tk.Text(
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000"
)
text_enddatum1 = "Enddatum eingeben \nDD.MM.YYYY"
enddatum1.insert(tk.END, text_enddatum1)                # Beschriftung in Textfeld einfügen
enddatum1.configure(state='disable')
enddatum1.place(x=10, y=120, width=150, height=50)

enddatum2 = tk.Text(
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000"
)
text_enddatum2 = "\nHH:MM"
enddatum2.insert(tk.END, text_enddatum2)                # Beschriftung in Textfeld einfügen
enddatum2.configure(state='disable')
enddatum2.place(x=160, y=120, width=150, height=50)

e3_enddatum = tk.Entry(                                 # Eingabe Enddatum (Datum)
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "left"
)
e3_enddatum.place(x=10, y=160, width=150, height=25)

e4_enddatum = tk.Entry(                                 # Eingabe Enddatum (Uhrzeit)
    bg = "#dddddd",
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "left"
)
e4_enddatum.place(x=160, y=160, width=150, height=25)

b_datum = tk.Button(bg = "#dddddd",                     # Dateneingabe (Start- & Enddatum) in jeweiliges Textfeld
    font = tkFont.Font(family='Times',size=10),
    fg = "#000000",
    justify = "center",
    text = "Datum übernehmen",
    command = datum_uebernehmen
)
b_datum.place(x=90, y=200, width=150, height=25)


### BAUTEILAUSWAHL
opt = tk.OptionMenu(root, var, *bauteil)                # Dropdownliste erstellen, *bauteil: alle Elemente aus Liste
opt.config(width=90, font=('Helvetica', 10))
opt.place(x=10, y=10, width=150, height=25)

def callback(*args):
    var.get()                           # var.get(): in Dropdownmenü ausgewählter Wert || label["text"] = var.get() ausgewählten Wert als Labeltitel
    #return

var.trace("w", callback)                                # nutzt callback-Fkt, um Varaiblenwert zu bekommen

root.mainloop()
