import json

printer_api ='{"sd":{"ready":true},"state":{"error":"","flags":{"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,"printing":false,"ready":false,"resuming":false,"sdReady":true},"text":"Paused"},"temperature":{"W":{"actual":0.0,"offset":0,"target":null},"bed":{"actual":64.94,"offset":0,"target":65.0},"tool0":{"actual":199.67,"offset":0,"target":200.0}}}'


def printer_api_f(octoprint_rest):
    job_info = octoprint_rest.get_job_info()
    y = json.loads(job_info)
    state = y["state"]
    flags = state['flags']
    state = {}
    for key, value in dict(flags).items():
        if value == False:
            del flags[key]
        else:
            name = key
            value = flags[key]
            state[name] = value

    temperatur = y['temperature']
    temp_bed_i = temperatur['bed']['actual']
    temp_bed_s = temperatur['bed']['target']
    temp_tool_i = temperatur['tool0']['actual']
    temp_tool_s = temperatur['tool0']['target']
    printer_api_data = {"state":state,"temp_tool_i":temp_tool_i,"temp_tool_s":temp_tool_s,"temp_bed_i":temp_bed_i,"temp_bed_s":temp_bed_s}
    return state,temp_tool_i,temp_tool_s,temp_bed_i,temp_bed_s

def job_api_f(octoprint_rest):
    job_info = octoprint_rest.get_job_info()
    y = json.loads(job_info)
    averagePrintTime =y["job"]['averagePrintTime']
    volume = y['job']['filament']['tool0']['volume']
    display = y['job']['file']['display']
    job_api_data = {'averagePrintTime':averagePrintTime,"volume":volume,"display":display}
    return averagePrintTime,volume,display

def files_api_f(octoprint_rest):
    job_info = octoprint_rest.get_job_info()
    y = json.loads(job_info)
    files = y['files']
    i = 0
    for key, value in y.items():
        if key == "files":
            i = i+1
    for n in range(0,i):
        file = files[n]

        free = y['free']
        display = file['display']
        hash = file['hash']
        download = file['refs']['download']
        files_api_data = {'hash':hash, 'display':display,'download':download,'free':free}
        return free, display, hash, download


#werte_printer_api = printer_api_f(printer_api)
#werte_job_api = job_api_f(job_api)
#werte_files_api = files_api_f(files_api)

