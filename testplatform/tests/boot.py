from testapi import *
from utilities import uefi_boot


def run(self):
    sleep(3)

    uefi_boot()

    assert_screen("boot", 100)


def test_flags(self):
    return {"milestone": 1}
