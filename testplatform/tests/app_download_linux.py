from testapi import *
from utilities import download_and_open_linux as download_and_open


def run(self):
    download_and_open()
    assert_screen("qalculate_open", 10)


def test_flags(self):
    return {"fatal": 1}
