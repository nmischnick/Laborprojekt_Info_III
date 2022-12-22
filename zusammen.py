from Datenbank.datenbank import create_database, to_database_all
from Datenbank.datenbank import storage_progress, count_states, temp_progress, get_all_files
from Octoprint.json_filter import files_api_f, printer_api_f, job_api_f
import threading
import datetime

create_database()

def dostuff():
    files = files_api_f()
    printer = printer_api_f()
    jobs = job_api_f()

    threading.Timer(10.0, dostuff).start()
    to_database_all(files, jobs, printer)


#dostuff()

print(get_all_files())
