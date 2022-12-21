"""
    Projekt - Labor IngInfo 3   Testcode
    Autor: J. Bode         Matr.-Nr. 70476607
"""
import datenabfrage
import datetime
import unittest
from unittest.mock import patch, MagicMock

teil = 0
job = 1
startdatum = datetime.datetime(2020, 12, 25, 13, 45).strftime("%d.%m.%Y %H:%M")       # Jahr, Monat, Tag, Stunde, Minute
enddatum = datetime.datetime(2021, 1, 10, 15, 12).strftime("%d.%m.%Y %H:%M")
#print("Start: ",startdatum," --- Ende:",enddatum)

mock = MagicMock()

class TestMain(unittest.TestCase):

    @patch('datenabfrage.get_Data.get_states')
    def test_get_states(self, mock):
        mock.return_value = {"error": 0, "ready": 0, "paused": 0, "printing": 0}
        self.assertEqual(datenabfrage.get_Data.get_states(startdatum, enddatum), {"error": 0, "ready": 0, "paused": 0, "printing": 0})

    @patch('datenabfrage.get_Data.get_storage')
    def test_get_storage(self, mock):
        mock.return_value = [[10, 20, 30], [50, 60, 70]]
        self.assertEqual(datenabfrage.get_Data.get_storage(startdatum, enddatum), [[10, 20, 30], [50, 60, 70]])

    @patch('datenabfrage.get_Data.get_temp')
    def test_get_temp(self, mock):
        mock.return_value = ((10, 30, 50, 60, 70), (20, 40, 60, 75, 80))    #((time, temp_tool_i, temp_tool_s, temp_bed_i, temp_bed_s),(...))
        self.assertEqual(datenabfrage.get_Data.get_temp(job), ((10, 30, 50, 60, 70), (20, 40, 60, 75, 80)))

    @patch('datenabfrage.get_Data.get_number')
    def test_get_number(self, mock):
        mock.return_value = "return-value"
        self.assertEqual(datenabfrage.get_Data.get_number(startdatum, enddatum, teil), "return-value")

    @patch('datenabfrage.get_Data.get_average_pt')
    def test_get_average_pt(self, mock):
        mock.return_value = "return-value"
        self.assertEqual(datenabfrage.get_Data.get_average_pt(), "return-value")

    @patch('datenabfrage.get_Data.get_average_pv')
    def test_get_average_pv(self, mock):
        mock.return_value = "return-value"
        self.assertEqual(datenabfrage.get_Data.get_average_pv(startdatum, enddatum), "return-value")
