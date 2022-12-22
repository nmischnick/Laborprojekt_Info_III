"""
    Projekt - Labor IngInfo 3
    Autor: J. Bode          Matr.-Nr. 70476607
"""

import Datenbank.datenbank as db


class get_Data():
    @staticmethod
    def get_states(start, ende):
        return db.count_states(start, ende)

    @staticmethod
    def get_storage(start, ende):
        return db.storage_progress(start, ende)              #App.dt_startdatum, App.dt_enddatum)

    @staticmethod
    def get_temp(job_id):
        tupel = db.temp_progress(job_id)
        liste4 = list(tupel)
        temp = []
        for i in range(len(liste4)):
            temp.append(list(liste4[i]))
        return temp

    @staticmethod
    def get_number(start, ende, teil):
        return db.object_count_period(start, ende, teil)

    @staticmethod
    def get_average_pt():
        return db.average_print_time()

    @staticmethod
    def get_average_pv(start, ende):
        return db.average_volume_period(start, ende)

    @staticmethod
    def get_name():
        tupel = db.get_all_files()          # ((job_id, dateiname, downloadlink),(...))
        liste = list(tupel)
        liste1 = []
        print(liste)
        for i in range(len(liste)):
            liste1.append(list(liste[i]))
        print(liste1)
        name = []
        for i in range(len(liste1)):
            name.append(liste1[i][1])
        return name

    @staticmethod
    def get_job():
        tupel = db.get_all_jobs()
        liste2 = list(tupel)
        liste3 = []
        print(liste2)
        for i in range(len(liste2)):
            liste3.append(list(liste2[i]))
        print(liste3)
        job_id = []
        for i in range(len(liste3)):
            job_id.append(liste3[i][0])
        return job_id

    @staticmethod
    def get_file():
        tupel = db.get_all_files()
        liste2 = list(tupel)
        liste3 = []
        print(liste2)
        for i in range(len(liste2)):
            liste3.append(list(liste2[i]))
        print(liste3)
        file_id = []
        for i in range(len(liste3)):
            file_id.append(liste3[i][0])
        return file_id

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