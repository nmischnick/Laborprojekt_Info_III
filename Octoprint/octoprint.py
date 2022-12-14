"""
Diese Datei ruft die Daten des Druckers über die octoprint API ab.

Autor: Nico Mischnick
letzte Änderung: 14.12.22
"""

import requests
import json

class get_data:

    def server_request(self, URL):

        response = requests.get(URL, timeout = 0.5)
        if response.status_code == 200:
            return response.json()
        raise Exception

    def check_json_error(self, data):
        try:
            jdata = json.loads(data)
            if "error" in jdata:
                return True
        except ValueError:
            return True
        return False
