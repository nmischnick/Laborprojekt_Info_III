""" UT: was macht dieses Modul, was machen die Funktionen?
        Wer hat es geschrieben, wann wurde es zuletzt geändert?
"""
from unittest.mock import MagicMock
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# UT: PEP8 beachten! sprechenden Variablennamen.
def random_int(a=0, b=200):
    return random.randint(a, b)

def random_float(a=0, b=200):
    return random.uniform(a, b)

display = id_generator()
date = random_int()


def sample_data_printer():
    state = id_generator()
    temp_tool_i = random_float()
    temp_tool_s = random_float()
    temp_bed_i = random_float()
    temp_bed_s = random_float()

    sample_data = {"state":state, "temp_tool_i": temp_tool_i, "temp_tool_s": temp_tool_s, "temp_bed_i": temp_bed_i, "temp_bed_s": temp_bed_s}

    return sample_data

def sample_data_job():
    averagePrintTime = random_float(0, 50)
    volume = random_float(0, 50)

    sample_data = {"averagePrintTime":averagePrintTime, "volume": volume, "display": display, "date": date}

    return sample_data

#

def sample_data_files():

    files = []

    for i in range(2):
        hash = id_generator(25)
        #display = id_generator()
        download = id_generator()
        free = random_int(10000000, 100000000)

        sample_data = {"hash": hash, "date": date, "display": display, "download": download, "free": free}

        files.append(sample_data)


    return files


def test_can_insert_data():
    octoprint = MagicMock()
    octoprint.get_printer_data.return_value = sample_data_printer()
    octoprint.get_files_data.return_value = sample_data_files()
    octoprint.get_jobs_data.return_value = sample_data_job()
    printer = octoprint.get_printer_data()
    files = octoprint.get_files_data()
    jobs = octoprint.get_jobs_data()
    #to_database_all(printer, files, jobs) # UT: das wäre die eigentliche Prüfung.

    assert True  # UT: hier fehlt die Prüfung! Es wird auch nicht mir den Rückgabewerten des Mocks
                 #     gearbeitet.

