"""
    Test für Klassen mit tkinter
    Autor: Jana Bode          Matr.-Nr. 70476607
           Sirine Gloulou     Matr.-Nr. 70457104
    Letzte Änderung: 22.12.2022
"""

### Imports
import datenabfrage
import Datenbank.datenbank as db
import tkinter as tk
import tkinter.messagebox as msg
import datetime
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


matplotlib.use('TkAgg')     # festlegen, welches Backend matplotlib nutzen soll

##############################################
db.create_database() # UT: Bei jedem Start der Applikation?
##############################################

root = tk.Tk()              # Fenster initialisieren


class App():
    ### Variablen für alles
    var = ""
    id = 24
    dt_startdatum = ""
    dt_enddatum = ""
    temp_t = []             # Leere Liste erstellen
    temp_tool_i = []
    temp_tool_s = []
    temp_bed_i = []
    temp_bed_s = []

    def __init__(self):
        root.title("Projekt - Labor Ingenieurinformatik 3")           # Fenstertitel festlegen
        root.geometry("600x600")                                      # Fenstergöße festlegen
        root.minsize(width=400, height=400)                           # minimale Fenstergröße
        root.maxsize(width=1200, height=1200)                         # maximale Fenstergröße
        root.resizable(width=True, height=True)                       # Größenänderung mit Maus möglich

        self.widgets_hauptfenster()                 # Aufrufen der Funktion aus Klasse

    def widgets_hauptfenster(self):
        """ Erzeugt alle Widgets für Startseite & platziert diese """

        ### Navigation
        self.b_statistic = tk.Button(root, bg="#dddddd", fg="#000000", justify="center", text="Statistic", command=self.b_statistic_command)  # Erzeugen eines Knopfes, command: Aufruf, der bei Anklicken erfolgt
        self.b_statistic.place(x=510, y=10, width=70, height=25)                # Platzierung des Knopfes auf Fenster

        ### Eingabe Start- und Enddatum
        self.start_ges = tk.Text(root, fg="#000000", state="disable")       # Erzeugen eines Textfeldes
        self.start_ges.place(x=320, y=40, width=180, height=70)             # Platzierung des Textfeldes auf Fenster

        self.ende_ges = tk.Text(root, fg="#000000", state="disable")
        self.ende_ges.place(x=320, y=120, width=180, height=70)

        text_startdatum1 = "Enter start date\nDD.MM.YYYY"               # Text, der in Textfeld später eingefügt wird
        self.startdatum1 = tk.Text(root, fg="#000000")
        self.startdatum1.place(x=10, y=40, width=150, height=50)
        self.startdatum1.insert(tk.END, text_startdatum1)               # Einfügen des Textes in Textfeld
        self.startdatum1.configure(state="disable")                     # Textfeld schreibgeschützt setzten

        text_startdatum2 = "\nHH:MM"
        self.startdatum2 = tk.Text(root, fg="#000000")
        self.startdatum2.place(x=160, y=40, width=150, height=50)
        self.startdatum2.insert(tk.END, text_startdatum2)
        self.startdatum2.configure(state="disable")

        self.e1_startdatum = tk.Entry(root, fg="#000000", justify="left")       # Erzeugen eines Eingabefeldes
        self.e1_startdatum.place(x=10, y=80, width=150, height=25)       # Platzierung des Feldes auf Fenster

        self.e2_startdatum = tk.Entry(root, fg="#000000", justify="left")
        self.e2_startdatum.place(x=160, y=80, width=150, height=25)

        text_enddatum1 = "Enter end date\nDD.MM.YYYY"
        self.enddatum1 = tk.Text(root, fg="#000000")
        self.enddatum1.place(x=10, y=120, width=150, height=50)
        self.enddatum1.insert(tk.END, text_enddatum1)
        self.enddatum1.configure(state="disable")

        text_enddatum2 = "\nHH:MM"
        self.enddatum2 = tk.Text(root, fg="#000000")
        self.enddatum2.insert(tk.END, text_enddatum2)
        self.enddatum2.configure(state="disable")
        self.enddatum2.place(x=160, y=120, width=150, height=50)

        self.e1_enddatum = tk.Entry(root, fg="#000000", justify="left")
        self.e1_enddatum.place(x=10, y=160, width=150, height=25)

        self.e2_enddatum = tk.Entry(root, fg="#000000", justify="left")
        self.e2_enddatum.place(x=160, y=160, width=150, height=25)

        self.b_datum = tk.Button(root, bg="#dddddd", fg="#000000", justify="center", text="Select date", command=self.datum)        # Erzeugen eines Knopfes
        self.b_datum.place(x=90, y=200, width=150, height=25)

        self.l_Anzahl = tk.Label(root, bg="#dddddd", fg="#000000", justify="center",text="Number of printed parts:\n")      # Erzeugen eines Labels
        self.l_Anzahl.place(x=10, y=250, width=150, height=50)                              # Platzierung des Labels auf Fenster

        self.l_Druckzeit = tk.Label(root, bg="#dddddd", fg="#000000", justify="center", text="Average print time:\n")
        self.l_Druckzeit.place(x=170, y=250, width=150, height=50)

        self.l_Druckvolumen = tk.Label(root, bg="#dddddd", fg="#000000", justify="center", text="Average print volume:\n")
        self.l_Druckvolumen.place(x=330, y=250, width=150, height=50)

        self.b_show = tk.Button(root, bg="#dddddd", fg="#000000", justify="center", text="Show", command=self.b_show_command)
        self.b_show.place(x=10, y=310, width=150, height=25)

        ### Bauteilauswahl
        bauteil = datenabfrage.get_Data.get_name()         # Auswahlmöglichkeiten für Dropdown-Liste --> eigentlich aus Datenbank abfragen
        self.var = tk.Variable(value=bauteil)                                       # Liste als Variablen für Dropdownliste festlegen
        self.var.set("Choose component")
        self.opt = tk.OptionMenu(root, self.var, *bauteil)                          # OptionsMenü erzeugen
        self.opt.config(width=90, font=('Helvetica', 10))                           # Konfigurationsoptionen für Optionsmenü
        self.opt.place(x=10, y=10, width=150, height=25)

        job_id = datenabfrage.get_Data.get_job()
        self.id = tk.Variable(value=job_id)                 # Liste als Variablen für Dropdownliste festlegen
        self.id.set("Choose job")
        self.opt2 = tk.OptionMenu(root, self.id, *job_id)   # OptionsMenü erzeugen
        self.opt2.config(width=90, font=('Helvetica', 10))  # Konfigurationsoptionen für Optionsmenü
        self.opt2.place(x=170, y=10, width=150, height=25)

    def b_statistic_command(self):
        """ Erzeugt ein zweites Fenster (Toplevel) und deren Widgets & Diagramme """

        auswahl = self.var.get()                # Inhalt von var abfragen
        if(auswahl == "Choose componenet"):     # Wenn kein Bauteil ausgewählt
            msg.showwarning("Warning","\nPlease choose a component!\n")     # Warnmeldung
        else:                                   # Wenn Bauteil ausgewählt
            newwin = tk.Toplevel(root)          # erzeugen eines 2. Fensters ("liegt" auf root)
            newwin.title("Statistics")
            newwin.geometry("600x600")
            newwin.minsize(width=400, height=400)
            newwin.maxsize(width=1200, height=1400)
            newwin.resizable(width=True, height=True)

            self.l_teil = tk.Label(newwin, bg="#dddddd", fg="#000000", justify="center")            # Text des erzeugten Labes entspricht Bauteilauswahl aus Dropdownliste (Hauptfenster)
            self.l_teil.place(x=10, y=10, width=250, height=25)
            self.l_teil["text"] = auswahl

            self.b_home = tk.Button(newwin, bg="#dddddd", fg="#000000", justify="center", text="Home", command=newwin.destroy)
            self.b_home.place(x=510, y=10, width=70, height=25)

            ### bar chart
            x_zeit = self.fs_time                  # Liste mit Zeitpunkten  --> theoretisch aus Datenbank
            y_speicher_frei = self.fs_storage         # Liste mit freiem Speicher --> theoretisch aus Datenbank
            figure = Figure(figsize=(5, 4), dpi=100)            # Figure erstellen, um Diagramm zu halten
            figure_canvas = FigureCanvasTkAgg(figure, master=newwin)    # Objekt, um Figure und Canvas zu verknüfen, Fenster festlegen
            NavigationToolbar2Tk(figure_canvas, newwin)                 # built-in Toolbar von mathplotlib
            ax = figure.add_subplot()                           # Subplot hinzufügen und Achsen festlegen
            ax.bar(x_zeit, y_speicher_frei)                     # Datensatz 2 und Diagrammtyp
            ax.set_title("Freier Speicherplatz")                # Diagrammtitel
            ax.set_ylabel("Speicherplatz")                      # y-Achsen-Beschriftung
            ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='center')
            ax.legend(["Belegt", "Frei"])                       # Inhalt für Legende
            figure_canvas.get_tk_widget().place(x=10, y=50, width=460, height=350)  # Diagramm auf Fenster platzieren

            ## line chart
            x_zeit = self.temp_t
            y_temp_duese_ist = self.temp_tool_i
            y_temp_duese_soll = self.temp_tool_s
            y_temp_bett_ist = self.temp_bed_i
            y_temp_bett_soll = self.temp_bed_s
            figure = Figure(figsize=(5,4), dpi=100)
            figure_canvas = FigureCanvasTkAgg(figure, master=newwin)
            NavigationToolbar2Tk(figure_canvas, newwin)
            axes = figure.add_subplot()
            axes.scatter(x_zeit, y_temp_duese_ist)
            axes.scatter(x_zeit, y_temp_duese_soll)
            axes.scatter(x_zeit, y_temp_bett_ist)
            axes.scatter(x_zeit, y_temp_bett_soll)
            axes.set_xlabel("Zeit [min]")                       # x-Achsen-Beschriftugn
            axes.set_ylabel("Temperatur [°C]")
            axes.set_xticklabels(x_zeit, rotation=45, ha='center')
            axes.legend(["Düsentemp. ist", "Düsentemp. soll", "Betttemp. ist", "Betttemp. soll"], loc="lower right")
            figure_canvas.get_tk_widget().place(x=10, y=410, width=460, height=300)

    # UT: Diese Funktion ist viel zu groß und kann so nach der TDD-Methodik nicht entstanden sein.
    def datum(self):
        """
        Abfrage der Daten aus datenabfrage.py (Zugriff auf Datenbank)
        Überprüfung und Konvertierung der Datumseinagbe
        """

        start1 = str(self.e1_startdatum.get())              # Inhalt des Eingabefeldes abfragen und als string speichern
        start2 = str(self.e2_startdatum.get())
        ende1 = str(self.e1_enddatum.get())
        ende2 = str(self.e2_enddatum.get())

        # UT: Struktur! Keine Funktionen in Funktionen deinieren. Wo ist der Testfall für diese Funktion?
        def datum_pruefen(a1, a2):
            t_a1 = a1.split(".")  # Zerlegung des Strings, Trennzeichen .  --> Einzelne Stücke in Liste gespeichert
            t_a2 = a2.split(":")  # Zerlegung des Strings, Trennzeichen :  --> Einzelne Stücke in Liste gespeichert
            tag = int(t_a1[0])    # Zuweisung der einzelnen Teilstücke
            monat = int(t_a1[1])
            jahr = int(t_a1[2])
            stunde = int(t_a2[0])
            minute = int(t_a2[1])
            a_ges = datetime.datetime(jahr, monat, tag, stunde, minute)  # Zusammensetzen des Datums & abspeichern vom Typ datetime
            return a_ges

        try:                                                    # Versuch das Datum korrekt zu zerlegen
            self.dt_startdatum = datum_pruefen(start1, start2)  # Erstellung Startdatum in datetime-Format
            self.dt_enddatum = datum_pruefen(ende1, ende2)      # Erstellung Enddatum in datetime-Format
        except ValueError:                                      # wenn Zerlegung nicht korrekt möglich
            msg.showwarning("Warning", "ValueError\nPlease check your entry!\n")  # Warnmeldung, wenn keine korrekte Zerlegung möglich
        if (self.dt_startdatum <= self.dt_enddatum):
            self.start_ges.configure(state="normal")                # Textfeld nicht mehr schreibgeschützt
            self.ende_ges.configure(state="normal")
            self.start_ges.delete("1.0", "end")                     # Inhalt des gesamten Textfeldes löschen
            self.ende_ges.delete("1.0", "end")
            text_start_ges = ("Selected start date:\n {}".format(self.dt_startdatum))  # einzusetzender Text -> inkl. Inhalt datetime
            text_ende_ges = ("Selected end date:\n {}".format(self.dt_enddatum))
            self.start_ges.insert(tk.END, text_start_ges)           # Einfügen des Textes in Textfeld
            self.ende_ges.insert(tk.END, text_ende_ges)
            self.start_ges.configure(state="disable")               # Textfeld schreibgeschützt
            self.ende_ges.configure(state="disable")
        else:
            msg.showwarning("Warning", "Selected end date are earlier than selected start date!\nPleas check your entry.")

        ### Einträge aus Datenbank einfügen
        self.stati_dict = datenabfrage.get_Data.get_states(self.dt_startdatum, self.dt_enddatum)
        print(self.stati_dict)

        self.ready = self.stati_dict["ready"]
        self.printing = self.stati_dict["printing"]
        self.off = self.stati_dict["off"]
        self.paused = self.stati_dict["paused"]
        self.error = self.stati_dict["error"]

        storage = datenabfrage.get_Data.get_storage(self.dt_startdatum, self.dt_enddatum)
        self.fs_time = storage[0]
        self.fs_storage = storage[1]
        temp = datenabfrage.get_Data.get_temp(self.id.get())
        for i in range(len(temp)):
            self.temp_t.append(temp[i][0])      # Zerlegung des tupels in Listen
            self.temp_tool_i.append(temp[i][1])
            self.temp_tool_s.append(temp[i][2])
            self.temp_bed_i.append(temp[i][3])
            self.temp_bed_s.append(temp[i][4])

    def b_show_command(self):
        """ Erstellung und Platzierung (Anzeigen) des Tortendiagramms und Label unter de^n Angaben """

        file_id = datenabfrage.get_Data.get_file()
        print("##################", file_id)
        file = datenabfrage.get_Data.get_filename(self.var.get())
        num = datenabfrage.get_Data.get_number(self.dt_startdatum, self.dt_enddatum, file_id)
        # UT: PEP8 beachten! Auch Kommentare gehören zur Zeilenlänge. Es geht ja um Lesbarkeit.
        self.l_Anzahl["text"] = "Number of printed parts:\n {}".format(num)   #Anzahl gedruckter Teile --> theoretisch aus Datenbank
        av_pt = datenabfrage.get_Data.get_average_pt(file)
        self.l_Druckzeit["text"] = "Average print time:\n {}".format(av_pt)
        av_pv = datenabfrage.get_Data.get_average_pv(self.dt_startdatum, self.dt_enddatum)
        self.l_Druckvolumen["text"] = "Average print volume:\n {}".format(av_pv)

        stati = ['Bereit', 'Aus', 'Druckt', 'Pausiert', 'Störung']
        anz = [self.ready, self.off, self.printing, self.paused, self.error]
        colour = ('#cbe8ba', '#c0c0c0', '#ffd783', '#a8c6fa', '#ff8a84')
        figure = Figure(figsize=(5, 5), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, master=root)
        NavigationToolbar2Tk(figure_canvas, root)
        axes = figure.add_subplot()
        axes.pie(anz, labels=stati, colors=colour, autopct='%1.1f%%')       # Erstellung des Tortendiagramms
        axes.set_title("Number of states")
        figure_canvas.get_tk_widget().place(x=10, y=350, width=400, height=200)


app = App()     # Aufruf der Klasse
root.mainloop()     # Mainloop-Methode auf Hauptfenster anwenden --> Fenster bleibt so lange geöffnet, bis man es schließt (X)