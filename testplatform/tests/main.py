from testapi import *


def run(self):
    perl.require("autotest.pm")

    if get_var("VERSION") == "Tumbleweed":
        perl.autotest.loadtest("boot.py")
        perl.autotest.loadtest("app_download_linux.py")
        perl.autotest.loadtest("app_run_linux.py")
        perl.autotest.loadtest("rollback.py")
        perl.autotest.loadtest("web_app.py")

    elif get_var("VERSION") == "Windows":
        perl.autotest.loadtest("boot_win.py")
        perl.autotest.loadtest("app_download_win.py")
        perl.autotest.loadtest("app_run_win.py")

    elif get_var("VERSION") == "ARM":
        perl.autotest.loadtest("tests/arm.py")

    elif get_var("VERSION") == "QAD":
        perl.autotest.loadtest("start_qad.py")


def test_flags(self):
    return {"fatal": 1}
