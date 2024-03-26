from testapi import *
from pylib.utilities import uefi_boot_arm

def run(self):

    sleep(15)

    send_key("up")
    sleep(1)
    send_key("ret")

    #uefi_boot_arm()

    assert_screen('boot', 200)

def test_flags(self):
    return {'fatal': 1}

