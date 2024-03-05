from testapi import *

def run(self):

    perl.require("autotest.pm")

    if (get_var("VERSION") == "Tumbleweed"):
        
        perl.autotest.loadtest("boot.py")
        perl.autotest.loadtest("app_download.py")

    elif (get_var("VERSION") == "Windows"):

        perl.autotest.loadtest("boot_win.py")
        perl.autotest.loadtest("win.py")

    elif (get_var("VERSION") == "ARM"):

        perl.autotest.loadtest("boot_arm.py")

def test_flags(self):
    return {'fatal': 1}

