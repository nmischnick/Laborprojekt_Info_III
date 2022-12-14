"""
Diese Datei enthält die Mocks für die Test um  die Json Strings in beötigte Werte zu Bearbeiten
Autor: Jure Baloh
Datum: 14.12.2022 10:34
"""

import json

def printer_api_f(octoprint_rest):
    """Die Mock-Funktion bearbeitet den Json_printer_api_string. Dabei werden die False Werte rausgelöscht."""
    job_info = octoprint_rest.get_job_info()
    json_info = json.loads(job_info)
    state = json_info["state"]
    flags = state['flags']
    state = {}
    for key,value in dict(flags).items():
        if value is False:
            del flags[key]
        else:
            name = key
            value = flags[key]
            state[name] = value

    temperatur = json_info['temperature']
    temp_bed_i = temperatur['bed']['actual']
    temp_bed_s = temperatur['bed']['target']
    temp_tool_i = temperatur['tool0']['actual']
    temp_tool_s = temperatur['tool0']['target']
    return state,temp_tool_i,temp_tool_s,temp_bed_i,temp_bed_s

def job_api_f(octoprint_rest):
    """Die Funktion bearbeitet den Json_job_api_string."""
    job_info = octoprint_rest.get_job_info()
    json_info = json.loads(job_info)
    average_print_time =json_info["job"]['averagePrintTime']
    volume = json_info['job']['filament']['tool0']['volume']
    display = json_info['job']['file']['display']
    return average_print_time,volume,display

def files_api_f(octoprint_rest):
    """Die Funktion bearveitet den Json_files_api_string. Da der String aus mehreren Bäumen besteht, werden die nacheinander bearbeitet."""
    job_info = octoprint_rest.get_job_info()
    json_info = json.loads(job_info)
    files = json_info['files']
    i = 0
    for key,_ in json_info.items():
        if key == "files":
            i = i+1
    for zaehler in range(0,i):
        file = files[zaehler]

        free = json_info['free']
        display = file['display']
        hash_data = file['hash']
        download = file['refs']['download']
        return free, display, hash_data, download
