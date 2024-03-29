"""
Diese Datei ruft die Daten des Druckers über die octoprint API ab.

Autor: Nico Mischnick
letzte Änderung: 21.12.22
"""

import json
import requests
import ast


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
        response = requests.get(url, timeout=0.5)   # holt Infos von angegebener URL, liefert timeout nach 0.5 Sek
        if response.status_code == 200:             # wenn Status 200, also in Ordnung ist, versuche json zurückzugeben
            return str(response.json())             # gebe json der URL zurück
        raise TimeoutError                          # wenn Status nicht gleich 200, dann gebe TimeoutError zurück

    @staticmethod
    def check_json_error(data):
        """
        Diese Funktion überprüft den Input, ob es ein JSON-String ist
        und ob der JSON-String einen Error enthält
        """
        try:
            data = ast.literal_eval(data)  # wertet die json Funktion mit trees richtig aus
            data = json.dumps(data)  # konvertiert den ausgewerteten Wert in den passenden JSON
            jdata = json.loads(data)       # prüfe, ob zurückgegebene Datei wirklich json ist
            if "error" in jdata.keys():                # wenn ja, prüfe, ob json einen Error enthält
                return True               # wenn Error, gebe True zurück
        except ValueError:
            return True                         # wenn kein json gebe True zurück
        return False                            # wenn json ohne Error, gebe False zurück

# UT: diese Funktion wurde nicht getestet --> TDD-Methode verletzt
def get_json(url):
    """
    Diese Funktion dient zum Abfangen von Verbindungsfehlern und falschen Strings.
    Über diese Funktion bekommt das json_filter Programm zugriff auf die JSON-Strings von dem Server
    """
    try:
        string = GetData.server_request(url)        # Versuche Verbindung über URL zu bekommen
    except TimeoutError:
        return "Error: Verbindungsfehler"           # Wenn TimeoutError gebe dies zurück
    if GetData.check_json_error(string) is False:   # Wenn Prüfung Error False, dann gebe string zurück
        return string
    return "Error: JSON_String"                     # Wenn Prüfung Error True, dann gebe dies zurück
