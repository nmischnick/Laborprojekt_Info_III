from Datenbank.datenbank import create_database, to_database_all
from Datenbank.datenbank import storage_progress, count_states, temp_progress, get_all_files, count_states
from Octoprint.json_filter import files_api_f, printer_api_f, job_api_f
import threading
import datetime

create_database()

def dostuff():
    files = files_api_f()
    printer = printer_api_f()
    jobs = job_api_f()
    # UT: der Thread sollte eigentlich nicht in der Callback-Funktion des Threads gestartet werden
    # Besser in Zeile 19
    threading.Timer(10.0, dostuff).start()
    to_database_all(files, jobs, printer)


#dostuff()

print(temp_progress(24))