"""
Diese Datei enthält die Tests um  die Json Strings in beötigte Werte zu bearbeiten
Autor: Jure Baloh
Datum: 14.12.2022
"""

from unittest.mock import MagicMock
import json
from Octoprint_Jure import printer_api_f
from Octoprint_Jure import job_api_f
from Octoprint_Jure import files_api_f

def test_can_call_printer_api():
    """Die Funktion testet, ob die printer_api Json-String aufgerugen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "sd":
        {"ready":true},
    "state":
        {"error":"","flags":
            {"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,
            "printing":false,"ready":false,"resuming":false,"sdReady":true},
            "text":"Paused"},
    "temperature":
        {"W":{"actual":0.0,"offset":0,"target":null},
            "bed":{"actual":64.94,"offset":0,"target":65.0},
            "tool0":{"actual":199.67,"offset":0,"target":200.0}}}    
    """
    octoprint_rest.get_job_info(octoprint_rest)
    octoprint_rest.get_job_info.assert_called()

def test_get_job_info_gets_json_printer_api():
    """Die Funktion testet ob der json_pritnter_api String gelesen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "sd":
        {"ready":true},
    "state":
        {"error":"","flags":
            {"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,
            "printing":false,"ready":false,"resuming":false,"sdReady":true},
            "text":"Paused"},
    "temperature":
        {"W":{"actual":0.0,"offset":0,"target":null},
            "bed":{"actual":64.94,"offset":0,"target":65.0},
            "tool0":{"actual":199.67,"offset":0,"target":200.0}}}
    """
    assert json.loads(octoprint_rest.get_job_info())

def test_printer_api_f_returns_values_printer_api():
    """Die Funktion testet ob der json_pritnter_api String richtig interpretiert wird"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value ="""{
    "sd":
        {"ready":true},
    "state":
        {"error":"","flags":
            {"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,
            "printing":false,"ready":false,"resuming":false,"sdReady":true},
            "text":"Paused"},
    "temperature":
        {"W":{"actual":0.0,"offset":0,"target":null},
            "bed":{"actual":64.94,"offset":0,"target":65.0},
            "tool0":{"actual":199.67,"offset":0,"target":200.0}}}    
    """
    state,temp_tool_i,temp_tool_s,temp_bed_i,temp_bed_s = printer_api_f(octoprint_rest)
    assert state != "" and temp_tool_i == 199.67 and temp_tool_s == 200 and temp_bed_i == 64.94 and temp_bed_s == 65

def test_can_call_job_api():
    """Die Funktion testet, ob die job_api Json-String aufgerugen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "job":
        {"averagePrintTime":4988.674538585007,"estimatedPrintTime":3135.1295167632998,
            "filament":
                {"tool0":{"length":2991.2771200002394,"volume":7.194864641049301}},
        "file":{"date":1657719794,"display":"Handyhalter_TQM_1.gcode","name":"Handyhalter_TQM_1.gcode",
            "origin":"local","path":"Handyhalter_TQM_1.gcode","size":1980023},
        "lastPrintTime":5049.7762020089995,"user":"Triltsch"},
    "progress":{"completion":0.2779260644952104,"filepos":5503,"printTime":109,"printTimeLeft":4943,"printTimeLeftOrigin":"average"},"state":"Paused"
    }
    """
    octoprint_rest.get_job_info(octoprint_rest)
    octoprint_rest.get_job_info.assert_called()

def test_get_job_info_gets_json_job_api():
    """Die Funktion testet ob der json_job_api String gelesen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "job":
        {"averagePrintTime":4988.674538585007,"estimatedPrintTime":3135.1295167632998,
            "filament":
                {"tool0":{"length":2991.2771200002394,"volume":7.194864641049301}},
        "file":{"date":1657719794,"display":"Handyhalter_TQM_1.gcode","name":"Handyhalter_TQM_1.gcode",
            "origin":"local","path":"Handyhalter_TQM_1.gcode","size":1980023},
        "lastPrintTime":5049.7762020089995,"user":"Triltsch"},
    "progress":{"completion":0.2779260644952104,"filepos":5503,"printTime":109,"printTimeLeft":4943,"printTimeLeftOrigin":"average"},"state":"Paused"
    }"""

    assert json.loads(octoprint_rest.get_job_info())

def test_job_api_f_returns_values_job_api():
    """Die Funktion testet ob der json_job_api String richtig interpretiert wird"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value ="""{
    "job":
        {"averagePrintTime":4988.674538585007,"estimatedPrintTime":3135.1295167632998,
            "filament":
                {"tool0":{"length":2991.2771200002394,"volume":7.194864641049301}},
        "file":{"date":1657719794,"display":"Handyhalter_TQM_1.gcode","name":"Handyhalter_TQM_1.gcode",
            "origin":"local","path":"Handyhalter_TQM_1.gcode","size":1980023},
        "lastPrintTime":5049.7762020089995,"user":"Triltsch"},
    "progress":{"completion":0.2779260644952104,"filepos":5503,"printTime":109,"printTimeLeft":4943,"printTimeLeftOrigin":"average"},"state":"Paused"
    }   
    """
    average_print_time,volume,display = job_api_f(octoprint_rest)
    assert average_print_time == 4988.674538585007  and volume == 7.194864641049301 and display == "Handyhalter_TQM_1.gcode"

def test_can_call_files_api():
    """Die Funktion testet, ob die files_api Json-String aufgerugen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "files":
        [{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
            "gcodeAnalysis":{"dimensions":
                {"depth":104.754,"height":18.0,"width":101.754},
            "estimatedPrintTime":1415.1325518024532,
            "filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},
         "printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},
        "hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5",
        "name":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},
        "refs":{"download":"http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "resource":"http://141.41.42.192/api/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"},
        "size":498343,
        "statistics":{"averagePrintTime":{},"lastPrintTime":{}}
        ,"type":"machinecode","typePath":["machinecode","gcode"]} ],
    "free":27833102336,"total":31119536128}

    """

    octoprint_rest.get_job_info(octoprint_rest)
    octoprint_rest.get_job_info.assert_called()

def test_get_job_info_gets_json_files_api():
    """Funkton testen ob die files_api gelesen werden kann"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value = """{
    "files":
        [{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
            "gcodeAnalysis":{"dimensions":
                {"depth":104.754,"height":18.0,"width":101.754},
            "estimatedPrintTime":1415.1325518024532,
            "filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},
         "printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},
        "hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5",
        "name":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},
        "refs":{"download":"http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "resource":"http://141.41.42.192/api/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"},
        "size":498343,
        "statistics":{"averagePrintTime":{},"lastPrintTime":{}}
        ,"type":"machinecode","typePath":["machinecode","gcode"]} ],
    "free":27833102336,"total":31119536128}"""

    assert json.loads(octoprint_rest.get_job_info())

def test_files_api_f_returns_values_files_api():
    """Die Funktion testet ob der json_files_api String richtig interpretiert wird"""
    octoprint_rest = MagicMock()
    octoprint_rest.get_job_info.return_value ="""{
    "files":
        [{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
            "gcodeAnalysis":{"dimensions":
                {"depth":104.754,"height":18.0,"width":101.754},
            "estimatedPrintTime":1415.1325518024532,
            "filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},
         "printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},
        "hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5",
        "name":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},
        "refs":{"download":"http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode",
        "resource":"http://141.41.42.192/api/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"},
        "size":498343,
        "statistics":{"averagePrintTime":{},"lastPrintTime":{}}
        ,"type":"machinecode","typePath":["machinecode","gcode"]} ],
    "free":27833102336,"total":31119536128}"""
    free,display,hash_data,download = files_api_f(octoprint_rest)
    assert free == 27833102336 and display == "Form-Kubus_0.2mm_PETG_MK3S_25m.gcode" and hash_data == "732bc17d3771299b1c86272d75e6fb1522f3bcd5" and download == "http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"
