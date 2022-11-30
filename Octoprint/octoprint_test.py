"""
Diese Datei enthält die Tests für octoprint

Autor: Nico Mischnick
letzte Änderung: 30.11.22
"""

from octoprint import Octoprint

def test_get_JSON():
    test = Warenkorb.Artikel("Testartikel",10)
    assert test.artikel == "Testartikel"
    assert test.preis == 10