"""
    Projekt - Labor IngInfo 3
    Autor: J. Bode          Matr.-Nr. 70476607
"""

import Datenbank.datenbank as db


class get_Data():

    def get_states(self, start, ende):
        return db.count_states(start, ende)

    def get_storage(self, start, ende):
        return db.storage_progress(start, ende)              #App.dt_startdatum, App.dt_enddatum)

    def get_temp(self):
        job = db.get_all_jobs()
        temp = db.temp_progress(job)
        return temp

    def get_number(self, start, ende, teil):
        return db.object_count_period(start, ende, teil)

    def get_average_pt(self):
        return db.average_print_time()

    def get_average_pv(self, start, ende):
        return db.average_volume_period(start, ende)


"""
def get_states(self):
    return db.count_states(self.dt_startdatum, self.dt_enddatum)

def get_data(self):
    ### Funktionene für Datenbankaufruf müssen gemockt werden ###
    auswahl = self.var.get()  # Inhalt von var (Bauteilauswahl) in Variablen speichern
    self.stati_dict = db.count_states(self.dt_startdatum, self.dt_enddatum)
    freier_speicher = db.storage_progress(self.dt_startdatum, self.dt_enddatum)
    fs_zeit = freier_speicher[0]  # Liste aus Datenbank zerlegen
    fs_speicher = freier_speicher[1]
    job = db.get_all_jobs()
    temp = db.temp_progress(job)
    self.temp_t = []  # Leere Liste erstellen
    self.temp_tool_i = []
    self.temp_tool_s = []
    self.temp_bed_i = []
    self.temp_bed_s = []
    for i in range(len(temp)):
        self.temp_t[i] = temp(i)(0)  # Zerlegung des tupels in Listen
        self.temp_tool_i[i] = temp(i)(1)
        self.temp_tool_s[i] = temp(i)(2)
        self.temp_bed_i[i] = temp(i)(3)
        self.temp_bed_s[i] = temp(i)(4)
"""