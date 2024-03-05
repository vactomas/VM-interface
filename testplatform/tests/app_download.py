from testapi import *
from pylib.utilities import download_and_open


def run(self):
    download_and_open()
    assert_screen("qalculate", 20)
    #assert_screen("qalculate_open", 10)


def test_flags(self):
    return {'fatal': 1}

