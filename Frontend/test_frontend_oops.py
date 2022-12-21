"""
    Projekt - Labor IngInfo 3   Testcode
    Autor: J. Bode         Matr.-Nr. 70476607
"""
import frontend_oop_fh as fh
import datetime
import unittest
from unittest.mock import patch, MagicMock

startdatum = datetime.datetime(2020, 12, 25, 13, 45).strftime("%d.%m.%Y %H:%M")       # Jahr, Monat, Tag, Stunde, Minute
enddatum = datetime.datetime(2021, 1, 10, 15, 12).strftime("%d.%m.%Y %H:%M")
#print("Start: ",startdatum," --- Ende:",enddatum)

mock = MagicMock()

class TestMain(unittest.TestCase):

    @patch('fh.App.get_Data.st_dict')
    def test_getData_st_dict(self, mock):
        mock.return_value = {"error": 0, "ready": 0, "paused": 0, "printing": 0}
        self.assertEqual(fh.App.widgets_hauptfenster(), {"error": 0, "ready": 0, "paused": 0, "printing": 0})
