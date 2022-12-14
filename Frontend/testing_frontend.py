"""
    Laborprojekt IngInfo 3
    Testcode Frontend
"""
import frontend_home as fh
import frontend_statistic as fs
from unittest.mock import patch
from pytest import raises

@patch("frontend_home")
def test_bauteilauswahl(mock_fe):
    mock_fe.return_value.connect.return_value = True
    check = fh.connection(db)
    assert check == True





"""
Beispiel aus Labor_Mock

@patch("OPC_UA_Server.Client")      # erzeugt Mock von Klasse Client aus UPC_UA_Server.py
def test_aufruf_ft_make_client(mock_opcua):
    # mock_client = MagicMock()                                   # Mock erzeugen
    # mock_client.Client.connect = MagicMock(return_value=True)   # Rückgabe des Mocks bei Aufruf der Funktion
    # monkeypatch.setattr("opcua.Client.connect", mock_client)    # Verknüpfung Mock & Funktionsaufruf
    mock_opcua.return_value.connect.return_value = True           # Return Value definieren 
    check = OPC_UA_Server.make_client(url)                        # gemockte Funktion aufrufen
    assert check == True                                          # Erwartungswert festlegen
"""