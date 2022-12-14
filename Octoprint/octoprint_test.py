"""
Diese Datei enthält die Tests und Mocks für octoprint

Autor: Nico Mischnick
letzte Änderung: 14.12.22
"""
import unittest
from unittest.mock import patch, MagicMock
from octoprint import get_data

JSON_printer_url = ""
JSON_printer = """{"sd":{"ready":true},"state":{"error":"","flags":{"cancelling":false,"closedOrError":false,"error":false,"finishing":false,"operational":true,"paused":true,"pausing":false,"printing":false,"ready":false,"resuming":false,"sdReady":true},"text":"Paused"},"temperature":{"W":{"actual":0.0,"offset":0,"target":null},"bed":{"actual":64.94,"offset":0,"target":65.0},"tool0":{"actual":199.67,"offset":0,"target":200.0}}}"""
JSON_job_url = "http://141.41.42.192/api/job?apikey=A7DBE849344A42A0B22C50CA22EC6210"
JSON_job = """{"job":{"averagePrintTime":4988.674538585007,"estimatedPrintTime":3135.1295167632998,"filament":{"tool0":{"length":2991.2771200002394,"volume":7.194864641049301}},"file":{"date":1657719794,"display":"Handyhalter_TQM_1.gcode","name":"Handyhalter_TQM_1.gcode","origin":"local","path":"Handyhalter_TQM_1.gcode","size":1980023},"lastPrintTime":5049.7762020089995,"user":"Triltsch"},"progress":{"completion":0.2779260644952104,"filepos":5503,"printTime":109,"printTimeLeft":4943,"printTimeLeftOrigin":"average"},"state":"Paused"}"""
JSON_files ="""{"files":[{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode„,"gcodeAnalysis":{"dimensions":{"depth":104.754,"height":18.0,"width":101.754},"estimatedPrintTime":1415.1325518024532,"filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},"printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5","name":"FormKubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"FormKubus_0.2mm_PETG_MK3S_25m.gcode","prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},"refs":{"download":"http://141.41.42.192/downloads/files/local/FormKubus_0.2mm_PETG_MK3S_25m.gcode","resource":"http://141.41.42.192/api/files/local/FormKubus_0.2mm_PETG_MK3S_25m.gcode"},"size":498343,"statistics":{"averagePrintTime":{},"lastPrintTime":{}},"type":"machinecode","typePath":["machinecode","gcode"]} ],"free":27833102336,"total":31119536128}"""
JSON_error_1 = """{'error': 'SerialException: device reports readiness to read but returned no data (device disconnected or multiple access on port?)', 'job': {'averagePrintTime': None, 'estimatedPrintTime': None, 'filament': None, 'file': {'date': None, 'display': None, 'name': None, 'origin': None, 'path': None, 'size': None}, 'lastPrintTime': None, 'user': None}, 'progress': {'completion': None, 'filepos': None, 'printTime': None, 'printTimeLeft': None, 'printTimeLeftOrigin': None}, 'state': 'Offline after error'}"""
JSON_error_2 = """{"error":"You don't have the permission to access the requested resource. It is either read-protected or not readable by the server."}"""

mock_response = MagicMock()
class test_octopi(unittest.TestCase):
    @patch('octoprint.requests')
    def test_connection(self, mock_requests):
        mock_response.status_code = 200
        mock_response.json.return_value = JSON_job
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_data.server_request(self, JSON_job_url), JSON_job)

    @patch('octoprint.requests')
    def test_server_request_timeout(self, mock_requests):
        mock_response.status_code = Exception
        mock_requests.get.side_effect = mock_response
        with self.assertRaises(Exception):
            get_data.server_request(self, JSON_job_url)

    @patch('octoprint.requests')
    def test_json_error1(self, mock_requests):
        mock_response.json = JSON_error_1
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_data.check_json_error(self, JSON_error_1), True)

    @patch('octoprint.requests')
    def test_json_error2(self, mock_requests):
        mock_response.json = JSON_error_2
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_data.check_json_error(self, JSON_error_2), True)

    @patch('octoprint.requests')
    def test_json_valid(self, mock_requests):
        mock_response.json = JSON_printer
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_data.check_json_error(self,JSON_printer), False)