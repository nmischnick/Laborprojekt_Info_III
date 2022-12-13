from unittest.mock import MagicMock

import pytest
"""
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
"""

def sample_data_printer():
    state = ""
    temp_tool_i = 0
    temp_tool_s = 0
    temp_bed_i = 0
    temp_bed_s = 0

    sample_data = {"state":state, "temp_tool_i": temp_tool_i, "temp_tool_s": temp_tool_s, "temp_bed_i": temp_bed_i, "temp_bed_s": temp_bed_s}

    return sample_data

def sample_data_job():
    averagePrintTime = 0
    volume= 0
    display = ""

    sample_data = {"averagePrintTime":averagePrintTime, "volume": volume, "display": display}

    return sample_data

#

def sample_data_files():
    hash = "af"
    display = ""
    download = ""
    free = 0
    files = []

    sample_data = {"hash": "df", "display": "test", "download": "downloadlink", "free": free}

    files.append(sample_data)

    sample_data1 = {"hash": "bf", "display": display, "download": download, "free": free}

    files.append(sample_data1)

    return files

@pytest.fixture()
def mock_octoprint():
    pass



def test_can_call_get_data():
    octoprint = MagicMock()
    octoprint.get_data.return_value = sample_data_printer()
    octoprint.get_data()
    octoprint.get_data.assert_called()