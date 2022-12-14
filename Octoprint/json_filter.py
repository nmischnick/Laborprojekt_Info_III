"""
Diese Datei bearbeitet die Json Strings in beötigte Werte
Autor: Jure Baloh
Datum: 14.12.2022
"""

import json
import octoprint
import ast

PRINTER_URL = "http://141.41.42.192/api/printer?apikey=A7DBE849344A42A0B22C50CA22EC6210"
JOB_URL = "http://141.41.42.192/api/job?apikey=A7DBE849344A42A0B22C50CA22EC6210"
FILES_URL = "http://141.41.42.192/api/files?apikey=A7DBE849344A42A0B22C50CA22EC6210"

PRINTER_API ='{"sd":{"ready":true},"state":{"error":"","flags":{"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,"printing":false,"ready":false,"resuming":false,"sdReady":true},"text":"Paused"},"temperature":{"W":{"actual":0.0,"offset":0,"target":null},"bed":{"actual":64.94,"offset":0,"target":65.0},"tool0":{"actual":199.67,"offset":0,"target":200.0}}}'
JOB_API = '{"job":{"averagePrintTime":4988.674538585007,"estimatedPrintTime":3135.1295167632998,"filament":{"tool0":{"length":2991.2771200002394,"volume":7.194864641049301}},"file":{"date":1657719794,"display":"Handyhalter_TQM_1.gcode","name":"Handyhalter_TQM_1.gcode","origin":"local","path":"Handyhalter_TQM_1.gcode","size":1980023},"lastPrintTime":5049.7762020089995,"user":"Triltsch"},"progress":{"completion":0.2779260644952104,"filepos":5503,"printTime":109,"printTimeLeft":4943,"printTimeLeftOrigin":"average"},"state":"Paused"}'
FILES_API = '{"files":[{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","gcodeAnalysis":{"dimensions":{"depth":104.754,"height":18.0,"width":101.754},"estimatedPrintTime":1415.1325518024532,"filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},"printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5","name":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},"refs":{"download":"http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","resource":"http://141.41.42.192/api/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"},"size":498343,"statistics":{"averagePrintTime":{},"lastPrintTime":{}},"type":"machinecode","typePath":["machinecode","gcode"]} ],"free":27833102336,"total":31119536128}'

def printer_api_f(json_str):
    "Die Funktion bearbeitet den Json_printer_api_string. Dabei werden die False Werte rausgelöscht."
    json_info = json.loads(json_str)            #json wird gelesen
    state = json_info["state"]                  # json baum wird definiert
    flags = state['flags']                      #json unterbaum wird definiert
    state = {}
    for key, value in dict(flags).items():
        if value is False:                      # wenn key = false wird entfernt
            del flags[key]
        else:                                   #wenn key "! false wird er in die dict hinzugefügt
            name = key
            value = flags[key]
            state[name] = value

    temperatur = json_info['temperature']       #daten definieren mit path
    temp_bed_i = temperatur['bed']['actual']
    temp_bed_s = temperatur['bed']['target']
    temp_tool_i = temperatur['tool0']['actual']
    temp_tool_s = temperatur['tool0']['target']
    printer_api_data = {"state":state,"temp_tool_i":temp_tool_i,"temp_tool_s":temp_tool_s,"temp_bed_i":temp_bed_i,"temp_bed_s":temp_bed_s} #daten in eigene Dict
    return printer_api_data

def job_api_f(json_str):
    "Die Funktion bearveitet den Json_job_api_string. Die wichtigen Werte werden im neuen Dict gespeichert."
    json_info = json.loads(json_str)                            #json wird gelesen
    average_print_time =json_info["job"]['averagePrintTime']      #daten definieren mit path
    volume = json_info['job']['filament']['tool0']['volume']
    display = json_info['job']['file']['display']
    job_api_data = {'averagePrintTime':average_print_time,"volume":volume,"display":display}  #daten in eigene Dict
    return job_api_data

def files_api_f(json_str):
    "Die Funktion bearveitet den Json_files_api_string. Da der String aus mehreren Bäumen besteht, werden die nacheinander bearbeitet."
    json_info = json.loads(json_str)    #json wird gelesen
    files = json_info['files']          #json baum wird definiert
    i = 0
    for key,_ in json_info.items():    #keys namens files in dict werden geuählt
        if key == "files":
            i = i+1
    for zaehler in range(0,i):
        file = files[zaehler]                     #der n baum files wird ausgewählt
        display = file['display']           #daten werden definiert mit path
        hash_data = file['hash']
        download = file['refs']['download']
        free = json_info['free']
        files_api_data = {'hash':hash_data, 'display':display,'download':download,'free':free} #daten in eigene dict
        return files_api_data

printer_api = octoprint.get_json(PRINTER_URL)
printer_api = ast.literal_eval(printer_api)
printer_api = json.dumps(printer_api)
werte_printer_api = printer_api_f(printer_api)

job_api = octoprint.get_json(JOB_URL)
job_api = ast.literal_eval(job_api)
job_api = json.dumps(job_api)
werte_job_api = job_api_f(job_api)

files_api = octoprint.get_json(FILES_URL)
files_api = ast.literal_eval(files_api)
files_api = json.dumps(files_api)
werte_files_api = files_api_f(files_api)

print(werte_printer_api)
print(werte_job_api)
print(werte_files_api)