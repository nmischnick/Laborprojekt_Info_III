"""
    Laborprojekt IngInfo 3
    Produktivcode Frontend - Startseite
"""

### IMPORTS

import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as msg
import datetime
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

### Fenster anlegen
#diagramme

root = tk.Tk()                       # Fenster-Instanz erzeugen
root.title("Projekt - Labor Ingenieurinformatik 3")         # Titel des Fensters
root.geometry("600x600")             # Fenster auf errechnete Größe skalieren
root.resizable(width=True, height=True)     # Fenstergröße variierbar mit Maus

class App:
    def __init__(self, master):
        global root
        global ft
        global var

        ft = tkFont.Font(family='Times', size=10)                   # Format für Schrift festlegen

        b_statistic = tk.Button(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Statistic")      # Erzeugen eines Knopfes
        b_statistic.place(x=510, y=10, width=70, height=25)  #grid(column=4, row=0) #       # Platzierung des Knopfes in Fenster
        """
        b_statistic=tk.Button(root)
        b_statistic["bg"] = "#dddddd"
        b_statistic["font"] = ft
        b_statistic["fg"] = "#000000"
        b_statistic["justify"] = "center"
        b_statistic["text"] = "Statistic"
        b_statistic.place(x=510, y=10, width=70, height=25)
        b_statistic.bind('<Button>', self.b_statistic_command)"""

    ### AUSWAHL START- & ENDDATUM
        start_ges = tk.Text(root, font=ft, fg="#000000", state="disable")       # Erzeugen eines Textfeldes
        start_ges.place(x=320, y=40, width=180, height=70) #grid(column=2, row=1)  # Platzierung des Textfeldes auf Fenster
        start_ges.configure(state="disable")                                    # Textfeld auf schreibgeschützt setzen
        """start_ges = tk.Text(root)
        start_ges["font"] = ft
        start_ges["fg"] = "#000000"
        start_ges.configure(state="disable")
        start_ges.place(x=320, y=40, width=180, height=70)"""

        ende_ges = tk.Text(root, font=ft, fg="#000000", state="disable")
        ende_ges.place(x=320, y=120, width=180, height=70)              # grid(column=2, row=2) #
        ende_ges.configure(state="disable")
        """
        ende_ges = tk.Text(root)
        ende_ges["font"] = ft
        ende_ges["fg"] = "#000000"
        ende_ges.configure(state="disable")
        ende_ges.place(x=320, y=120, width=180, height=70)"""

        text_startdatum1 = "Enter start date\nDD.MM.YYYY"                        # Text, der in Textfeld eingefügt wird
        startdatum1 = tk.Text(root, font=ft, fg="#000000")
        startdatum1.place(x=10, y=40, width=150, height=50)                      # grid(column=0, row=1) #
        startdatum1.insert(tk.END, text_startdatum1)                             # Einfügen des Textes in Textfeld
        startdatum1.configure(state="disable")                                   # Textfeld schreibgeschützt
        """
        startdatum1 = tk.Text(root)
        startdatum1["font"] = ft
        startdatum1["fg"] = "#000000"
        text_startdatum1 = "Enter start date\nDD.MM.YYYY"
        startdatum1.insert(tk.END, text_startdatum1)
        startdatum1.configure(state="disable")
        startdatum1.place(x=10, y=40, width=150, height=50)"""

        text_startdatum2 = "\nHH:MM"
        startdatum2 = tk.Text(root, font=ft, fg="#000000")
        startdatum2.place(x=160, y=40, width=150, height=50)                #grid(column=1, row=1)
        startdatum2.insert(tk.END, text_startdatum2)
        startdatum2.configure(state="disable")
        """
        startdatum2 = tk.Text(root)
        startdatum2["font"] = ft
        startdatum2["fg"] = "#000000"
        text_startdatum2 = "\nHH:MM"
        startdatum2.insert(tk.END, text_startdatum2)
        startdatum2.configure(state="disable")
        startdatum2.place(x=160, y=40, width=150, height=50)"""

        e1_startdatum = tk.Entry(root, font=ft, fg="#000000", justify="left")       # Erzeugen eines Eingabefeldes
        e1_startdatum.place(x=10, y=80, width=150, height=25)  #grid(column=0, row=2)     # Platzierung des Feldes auf Fenster
        """e1_startdatum=tk.Entry(root)
        e1_startdatum["font"] = ft
        e1_startdatum["fg"] = "#000000"
        e1_startdatum["justify"] = "left"
        e1_startdatum.place(x=10, y=80, width=150, height=25)"""

        e2_startdatum = tk.Entry(root, font=ft, fg="#000000", justify="left")
        e2_startdatum.place(x=160, y=80, width=150, height=25)         #grid(column=1, row=2) #
        """e2_startdatum = tk.Entry(root)
        e2_startdatum["font"] = ft
        e2_startdatum["fg"] = "#000000"
        e2_startdatum["justify"] = "left"
        e2_startdatum.place(x=160, y=80, width=150, height=25)"""

        text_enddatum1 = "Enter end date\nDD.MM.YYYY"
        enddatum1 = tk.Text(root, font=ft, fg="#000000")
        enddatum1.place(x=10, y=120, width=150, height=50)              #grid(column=0, row=3) #p
        enddatum1.insert(tk.END, text_enddatum1)
        enddatum1.configure(state="disable")
        """enddatum1 = tk.Text(root)
        enddatum1["font"] = ft
        enddatum1["fg"] = "#000000"
        text_enddatum1 = "Enter end date\nDD.MM.YYYY"
        enddatum1.insert(tk.END, text_enddatum1)
        enddatum1.configure(state="disable")
        enddatum1.place(x=10, y=120, width=150, height=50)"""

        text_enddatum2 = "\nHH:MM"
        enddatum2 = tk.Text(root, font=ft, fg="#000000")
        enddatum2.insert(tk.END, text_enddatum2)
        enddatum2.configure(state="disable")
        enddatum2.place(x=160, y=120, width=150, height=50)                         #grid(column=1, row=3) #
        """enddatum2 = tk.Text(root)
        enddatum2["font"] = ft
        enddatum2["fg"] = "#000000"
        text_enddatum2 = "\nHH:MM"
        enddatum2.insert(tk.END, text_enddatum2)
        enddatum2.configure(state="disable")
        enddatum2.place(x=160, y=120, width=150, height=50)"""

        e1_enddatum = tk.Entry(root, font=ft, fg="#000000", justify="left")
        e1_enddatum.place(x=10, y=160, width=150, height=25)                        #grid(column=0, row=4) #
        """e1_enddatum = tk.Entry(root)
        e1_enddatum["font"] = ft
        e1_enddatum["fg"] = "#000000"
        e1_enddatum["justify"] = "left"
        e1_enddatum.place(x=10, y=160, width=150, height=25)"""

        e2_enddatum = tk.Entry(root, font=ft, fg="#000000", justify="left")
        e2_enddatum.place(x=160, y=160, width=150, height=25)                       #grid(column=1, row=4) #
        """e2_enddatum = tk.Entry(root)
        e2_enddatum["font"] = ft
        e2_enddatum["fg"] = "#000000"
        e2_enddatum["justify"] = "left"
        e2_enddatum.place(x=160, y=160, width=150, height=25)"""

        b_datum = tk.Button(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Select date")        # Erzeugen eines Knopfes
        b_datum.place(x=90, y=200, width=150, height=25)           #grid(column=1, row=5) #                   # Platzierung auf Fenster
        """b_datum =tk.Button(root)
        b_datum["bg"] = "#dddddd"
        b_datum["font"] = ft
        b_datum["fg"] = "#000000"
        b_datum["justify"] = "center"
        b_datum["text"] = "Select date"
        b_datum.place(x=90, y=200, width=150, height=25)"""

        l_Anzahl = tk.Label(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Number of printed parts:\n")      # Erzeugen eines Labels
        l_Anzahl.place(x=10, y=250, width=150, height=50)             #grid(column=0, row=6) #                                 # Platzierung auf Fenster
        """l_Anzahl["bg"] = "#dddddd"
        l_Anzahl["font"] = ft
        l_Anzahl["fg"] = "#000000"
        l_Anzahl["justify"] = "center"
        l_Anzahl["text"] = "Number of prinzed parts:\n"    #{}".format(Wert-aus-Datenbank)
        l_Anzahl.place(x=10, y=250, width=150, height=50)"""

        l_Druckzeit = tk.Label(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Average print time:\n")
        l_Druckzeit.place(x=170, y=250, width=150, height=50)       #grid(column=1, row=6) #
        """l_Druckzeit["bg"] = "#dddddd"
        l_Druckzeit["font"] = ft
        l_Druckzeit["fg"] = "#000000"
        l_Druckzeit["justify"] = "center"
        l_Druckzeit["text"] = "Average print time:\n"    #{}".format(Wert-aus-Datenbank)
        l_Druckzeit.place(x=170, y=250, width=150, height=50)"""

        l_Druckvolumen = tk.Label(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Average print volume:\n")
        l_Druckvolumen.place(x=330, y=250, width=150, height=50)     #grid(column=2, row=6) #
        """l_Druckvolumen = tk.Label(root)
        l_Druckvolumen["bg"] = "#dddddd"
        l_Druckvolumen["font"] = ft
        l_Druckvolumen["fg"] = "#000000"
        l_Druckvolumen["justify"] = "center"
        l_Druckvolumen["text"] = "Average print volume:\n"  # {}".format(Wert-aus-Datenbank)
        l_Druckvolumen.place(x=330, y=250, width=150, height=50)"""

        b_pie = tk.Button(root, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Show pie")
        b_pie.place(x=10, y=310, width=150, height=25)     #grid(column=0, row=7) #
        """b_pie["bg"] = "#dddddd"
        b_pie["font"] = ft
        b_pie["fg"] = "#000000"
        b_pie["justify"] = "center"
        b_pie["text"] = "Show Pie"
        b_pie.place(x=10, y=310, width=150, height=25)"""

        ### Bauteilauswahl
        bauteil = ("Doppel-T-Träger", "T-Träger", "L-Träger", "Vollwelle")              # Auswahlmöglichkeiten für Dropdown-Liste --> aus Datenbank abfragen
        var = tk.Variable(value=bauteil)                                                # Liste als Variablen für Dropdownliste festlegen
        var.set("Choose component")                                                     # Standardwert festlegen (Wird vor Auswahl angezeigt)

        opt = tk.OptionMenu(root, var, *bauteil)                # OptionsMenü erzeugen
        opt.config(width=90, font=('Helvetica', 10))            # Konfigurationsoptionen für Optionsmenü
        opt.place(x=10, y=10, width=150, height=25)             # Optionsmenü auf Fenster platzieren    #grid(column=0, row=0)

    ### Funktionen + Bindungen
        def b_statistic_command(_event):                        # Funktion für Klicken des Navigationsknopfes 'Statistic'
            auswahl = var.get()                                 # Auswahl aus Dropdownliste abfragen
            if(auswahl != "Choose component"):                  # wenn Option ausgewählt wurde
                newwin = tk.Toplevel(root)                                      # Zweites Fenster (an Hauptfenster root geknüpft)
                newwin.title = ("Projekt - Labor Ingenieurinformatik 3")        # Titel für 2. Fenster
                newwin.geometry("600x600")  #alignstr)
                newwin.resizable(width=False, height=False)                     # keine Vergrößerung des Fensters zugelassen

                b_home = tk.Button(newwin, bg="#dddddd", font=ft, fg="#000000", justify="center", text="Home", command=newwin.destroy)  # Erzeugt Knopf auf 2. Fenster, der das Fenster bei Anklicken schließt
                b_home.place(x=510, y=10, width=70, height=25)    #grid(column=4, row=0) #
                """b_home = tk.Button(newwin)
                b_home["bg"] = "#dddddd"
                b_home["font"] = ft
                b_home["fg"] = "#000000"
                b_home["justify"] = "center"
                b_home["text"] = "Home"
                b_home["command"] = newwin.destroy()
                b_home.place(x=510, y=10, width=70, height=25)"""

                l_teil = tk.Label(newwin, bg="#dddddd", font=ft, fg="#000000", justify="center", text=var.get())            # Text des erzeugten Labes entspricht Bauteilauswahl aus Dropdownliste (Hauptfenster)
                l_teil.place(x=10, y=10, width=150, height=25)    #grid(column=0, row=0) #
                """l_teil["bg"] = "#dddddd"
                l_teil["font"] = ft
                l_teil["fg"] = "#000000"
                l_teil["justify"] = "center"
                l_teil["text"] = var.get()
                l_teil.place(x=10, y=10, width=150, height=25)"""

            else:
                msg.showwarning("Warning", "\nPlease choose a component!\n")                  # Wenn kein Bauteil ausgewählt wurde: Warnmeldung

        def b_datum_uebernehmen(_event):
            ### EINGABE PRÜFEN
            start1 = str(e1_startdatum.get())           # Werte aus Eingabefeld als string speichern
            start2 = str(e2_startdatum.get())
            ende1 = str(e1_enddatum.get())
            ende2 = str(e2_enddatum.get())

            def datum_pruefen(a1, a2):
                t_a1 = a1.split(".")                    # Zerlegung des Strings, Trennzeichen .  --> Einzelne Stücke in Liste gespeichert
                t_a2 = a2.split(":")                    # Zerlegung des Strings, Trennzeichen :  --> Einzelne Stücke in Liste gespeichert
                tag = int(t_a1[0])                      # Zuweisung der einzelnen Teilstücke
                monat = int(t_a1[1])
                jahr = int(t_a1[2])
                stunde = int(t_a2[0])
                minute = int(t_a2[1])
                a_ges = datetime.datetime(jahr, monat, tag, stunde, minute)     # Zusammensetzen des Datums & abspeichern vom Typ datetime
                dt_datum = a_ges.strftime("%d.%m.%Y %H:%M")     # Formatierung des datetime-Wertes
                return dt_datum
            try:    # Versuch das Datum korrekt zu zerlegen
                dt_startdatum = datum_pruefen(start1, start2)   # Erstellung Startdatum in datetime-Format
                dt_enddatum = datum_pruefen(ende1, ende2)       # Erstellung Enddatum in datetime-Format
            except ValueError:  # wenn Zerlegung nicht korrekt möglich
                msg.showwarning("Warning", "ValueError\nPlease check your entry!\n")        # Warnmeldung, wenn keine korrekte Zerlegung möglich

            ### EINGABE ANZEIGEN
            start_ges.configure(state="normal")             # Textfeld nicht mehr schreibgeschützt
            ende_ges.configure(state="normal")
            start_ges.delete("1.0", "end")                  # Inhalt des gesamten textfeldes löschen
            ende_ges.delete("1.0", "end")
            text_start_ges = ("Selected start date:\n {}".format(dt_startdatum))    # einzusetzender Text -> inkl. Inhalt datetime
            text_ende_ges = ("Selected end date:\n {}".format(dt_enddatum))
            start_ges.insert(tk.END, text_start_ges)        # Einfügen des Textes in Textfeld
            ende_ges.insert(tk.END, text_ende_ges)
            start_ges.configure(state="disable")            # Textfeld schreibgeschützt
            ende_ges.configure(state="disable")

            ### WERTE ANZEIGEN
            # stk = //Funktionsaufruf aus Datenbank.py um Stückzahl zu bekommen//
            # druckt = //Funktionsaufruf aus Datenbank.py um Druckzeit zu bekommen//
            # druckv = //Funktionsaufruf aus Datenbank.py um Druckvolumen zu bekommen//
            # l_Anzahl["text"] = "Number of printed parts:\n {}".format(stk)           # Aus Datenbank erhaltenen Wert in Label einfügen
            # l_Druckzeit["text"] = "Average print time:\n {}".format(druckt)
            # l_Druckvolumen["text"] = "Average print volume:\n {}".format(druckv)

            ### DIAGRAMM ANTEIL STATI
            def diagramm(_event):
                # Reihenfolge immer Bereit, Aus, Druckt, Pausiert, Störung
                stati = ['Bereit', 'Aus', 'Druckt', 'Pausiert', 'Störung']
                #state_dict = count_states()  //Funktionsaufruf aus Datenbank.py um Dictionary mit Anzahl der Stati zu bekommen//
                #anz = [state_dict["ready"], state_dict["off"], state_dict["printing"], state_dict["paused"], state_dict["error"]]     # Einfügen der Anzahl des jewiligen Stati
                anz = [5, 1, 3, 2, 1]
                colour = ('#cbe8ba', '#c0c0c0', '#ffd783', '#a8c6fa', '#ff8a84')
                plt.pie(anz, labels=stati, colors=colour ,autopct='%1.1f%%')            # Tortendiagramm erzeugen
                plt_save = plt.savefig("pltstati.png") #, dpi=75)                          # Tortendiagramm als Bild (.jpg) speichern

                image = Image.open("pltstati.png")                    # Bild öffnen
                test = ImageTk.PhotoImage(image)

                l_bild = tk.Label(root, image=test)                   # Bild als Label einfügen
                l_bild.image = test
                l_bild.place(x=10, y=350)                             # Platzierung auf Fenster     #grid(column=0, row=9, columnspan=4) #

            b_pie.bind('<Button>', diagramm)            # Knopf b_pie an Funktion 'diagramm' binden -> wird bei Klicken ausgeführt

        b_statistic.bind('<Button>', b_statistic_command)   # Knopf b_statistic an Funktion 'b_statistic_command' bnden
        b_datum.bind('<Button>', b_datum_uebernehmen)       # Knopf b_datum an Funktion 'b_datum_uebernehmen' binden

app = App(root)             # Aufruf der Klasse, root (Hauptfenster) als Übergabewert
root.mainloop()             # Mainloop-Methode auf Hauptfenster anwenden --> Fenster bleibt so lange geöffnet, bis man es schließt (X)


