from testapi import *
from utilities import uefi_boot


def run(self):
    sleep(3)

    uefi_boot()

    assert_screen("boot", 120)


def test_flags(self):
    return {"fatal": 1}
