"""
Diese Datei bearbeitet die Json Strings in beötigte Werte
Autor: Jure Baloh
Datum: 21.12.2022
"""
import ast
import json
from Octoprint.octoprint import get_json

PRINTER_URL = "http://141.41.42.192/api/printer?apikey=A7DBE849344A42A0B22C50CA22EC6210"
JOB_URL = "http://141.41.42.192/api/job?apikey=A7DBE849344A42A0B22C50CA22EC6210"
FILES_URL = "http://141.41.42.192/api/files?apikey=A7DBE849344A42A0B22C50CA22EC6210"

def printer_api_f():
    "Die Funktion ruft den String vom Server bearbeitet den Json_printer_api_string. Dabei werden die False Werte rausgelöscht."
    printer_api = get_json(PRINTER_URL)  # json str wird aufgerufen
    printer_api = ast.literal_eval(printer_api)  # wertet die json Funktion mit trees richtig aus
    printer_api = json.dumps(printer_api)  # konvertiert den ausgewerteten Wert in den passenden JSON
    json_info = json.loads(printer_api)            #json wird gelesen
    state = json_info["state"]                  # json baum wird definiert
    flags = state['flags']                      #json unterbaum wird definiert
    state = ""
    for key, value in dict(flags).items():
        if value is False:                      # wenn key = false wird entfernt
            del flags[key]
        elif key in ["error", "printing", "paused", "ready"]:                                   #wenn key != false wird er in die dict hinzugefügt

            state = key

    if state == "":
        state = "ready"

    temperatur = json_info['temperature']       #daten definieren mit path
    temp_bed_i = temperatur['bed']['actual']
    temp_bed_s = temperatur['bed']['target']
    temp_tool_i = temperatur['tool0']['actual']
    temp_tool_s = temperatur['tool0']['target']
    printer_api_data = {"state":state,"temp_tool_i":temp_tool_i,"temp_tool_s":temp_tool_s,"temp_bed_i":temp_bed_i,"temp_bed_s":temp_bed_s} #daten in eigene Dict
    return printer_api_data

def job_api_f():
    "Die Funktion ruft den String vom Server und bearbeitet den Json_job_api_string. Die wichtigen Werte werden im neuen Dict gespeichert."
    job_api = get_json(JOB_URL)
    job_api = ast.literal_eval(job_api)
    job_api = json.dumps(job_api)
    json_info = json.loads(job_api)                            #json wird gelesen
    average_print_time =json_info["job"]['averagePrintTime']      #daten definieren mit path
    volume = json_info['job']['filament']['tool0']['volume']
    display = json_info['job']['file']['display']
    date = json_info['job']['file']['date']
    job_api_data = {'averagePrintTime':average_print_time,"volume":volume,"date":date,"display":display}  #daten in eigene Dict
    return job_api_data

def files_api_f():
    "Die Funktion ruft den String vom Server bearbeitet den Json_files_api_string. Da der String aus mehreren Bäumen besteht, werden die nacheinander bearbeitet."
    files_api = get_json(FILES_URL)
    files_api = ast.literal_eval(files_api)
    files_api = json.dumps(files_api)
    json_info = json.loads(files_api)    #json wird gelesen
    files = json_info['files']          #json baum wird definiert
    liste =[]
    for i in range(0,len(files)):
        file = files[i]                     #der n tree des Files wird ausgewählt
        # UT: Sie machen hier immer wieder das gleiche --> in Funktion auslagern
        #     diese Funktion ist viel zu lang zum Testen. TDD-Methode beachten
        try:
            date = file['date']
        except: # UT: besser konkreten Fehler abfangen.
            date = None
        try:
            display = file['display']           #daten werden definiert mit path
        except:
            display = None
        try:
            hash_data = file['hash']
        except:
            hash_data = None
        try:
            download = file['refs']['download']
        except:
            download = None
        try:
            free = json_info['free']
        except:
            free= None
        try:
            success = json_info['prints']['success']
        except:
            success = None
        files_api_data = {'date': date, 'hash':hash_data, 'display':display,'download':download,'free':free,'success':success} #daten in eigene dict
        liste.append(files_api_data)
    return liste


