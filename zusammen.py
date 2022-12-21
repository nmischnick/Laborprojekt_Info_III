from Datenbank.datenbank import create_database, to_database_all
from Octoprint.json_filter import files_api_f, printer_api_f, job_api_f


create_database()

files = files_api_f()
printer = printer_api_f()
jobs = job_api_f()

#to_database_files(files)
to_database_all(files, jobs, printer)