"""
Diese Datei ruft die Daten des Druckers über die octoprint API ab.

Autor: Nico Mischnick
letzte Änderung: 14.12.22
"""

import json
import requests


class GetData:
    """
    Diese Klasse enthält Funktionen, um die Verbindung zum Server zu testen
    und einen gültigen JSON-String zu erhalten.
    """

    @staticmethod
    def server_request(url):
        """
        Diese Funktion testet die Verbindung zum Server.
        """
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return response.json()
        raise Exception

    @staticmethod
    def check_json_error(data):
        """
        Diese Funktion überprüft den Input, ob es ein JSON-String ist
        und ob der JSON-String einen Error enthält
        """
        try:
            jdata = json.loads(data)
            if "error" in jdata:
                return True
        except ValueError:
            return True
        return False
