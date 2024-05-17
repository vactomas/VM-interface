from testapi import *
from pylib.utilities import download_and_open_arm as download_and_open


def run(self):
    download_and_open()
    assert_screen("arm_open", 10)


def test_flags(self):
    return {"fatal": 1}
