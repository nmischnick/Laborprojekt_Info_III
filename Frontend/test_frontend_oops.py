"""
    Projekt - Labor IngInfo 3   Testcode
    Autor: Jana Bode         Matr.-Nr. 70476607
           Sirnie Gloulou    Matr.-Nr. 70457104
"""
import datenabfrage
import datetime
import unittest
from unittest.mock import patch, MagicMock



teil = "Teil"
job = 1
startdatum = datetime.datetime(2020, 12, 25, 13, 45).strftime("%d.%m.%Y %H:%M")       # Jahr, Monat, Tag, Stunde, Minute
enddatum = datetime.datetime(2021, 1, 10, 15, 12).strftime("%d.%m.%Y %H:%M")


mock = MagicMock()

class TestMain(unittest.TestCase):
    # UT: Es ist natürlich nicht sinnvoll, Ihre eigenen Funktionen, die Sie testen wollen zu mocken ;-).
    #     Sie hätten in diesem Fall Datenbank.datenbank.count_states(start, ende) mocken sollen.
    #     Besseres Beispiel siehe test_get_name
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
        mock.return_value = 10
        self.assertEqual(datenabfrage.get_Data.get_number(startdatum, enddatum, teil), 10)

    @patch('datenabfrage.get_Data.get_average_pt')
    def test_get_average_pt(self, mock):
        mock.return_value = 5
        self.assertEqual(datenabfrage.get_Data.get_average_pt(), 5)

    @patch('datenabfrage.get_Data.get_average_pv')
    def test_get_average_pv(self, mock):
        mock.return_value = 25
        self.assertEqual(datenabfrage.get_Data.get_average_pv(startdatum, enddatum), 25)
    # UT: hier wird richtig deutlich, dass der Test so nicht sinnvoll ist.
    #     Sie implementieren in datenabfrage.get_Data.get_name viel Code und einige Operationen.
    #     Sinn dieses tests ist es doch herauszufinden, ob diese Operationen das Richtge mit dem
    #     Ergebnis der DB Abfrage machen. Sie testen hier gar nichts, sondern geben einen festen Wert zurück.
    #     @patch('Datenbank.datenbank.get_all_files') wäre hier sinnvoll
    #     dann: mock.return_value = eine typische Rückgabe von Datenbank.datenbank.get_all_files()
    #     in dem Assert statement dann der verarbeitete return in Ihrem erwartetem Format.
    @patch('datenabfrage.get_Data.get_name')
    def test_get_name(self, mock):
        mock.return_value = ["teil1", "teil2", "teil3"]
        self.assertEqual(datenabfrage.get_Data.get_name(), ["teil1", "teil2", "teil3"])

    @patch('datenabfrage.get_Data.get_job')
    def test_get_all_jobs(self, mock):
        mock.return_value = ((24, "teil", "str"))     #((job_id, dateiname, downloadlink),(...))
        self.assertEqual(datenabfrage.get_Data.get_job(), ((24, "teil", "str")))

    @patch('datenabfrage.get_Data.get_file')
    def test_get_file(self, mock):
        mock.return_value = "str"
        self.assertEqual(datenabfrage.get_Data.get_file(), "str")

    @patch('datenabfrage.get_Data.get_filename')
    def test_get_filename(self, mock):
        mock.return_value = 12.03
        self.assertEqual(datenabfrage.get_Data.get_filename(teil), 12.03)