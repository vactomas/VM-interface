from testapi import *


def run(self):
    download_and_open()
    assert_screen("arm_open", 10)


def download_and_open():
    # Open Terminal
    open_app("Terminal")
    assert_screen("terminal_opened", 2)

    # Get variables from test settings
    app_name = get_var("APP")
    app_name_run = get_var("APP_RUN")
    url = get_var("URL")

    # Download app
    type_string(f"wget {url}\n")
    sleep(10)

    # Untar
    type_string(f"tar -xf {app_name}")
    send_key("tab")
    send_key("ret")
    sleep(10)

    # Open app folder
    type_string(f"cd {app_name}")
    send_key("tab")
    send_key("ret")
    sleep(1)


def test_flags(self):
    return {"fatal": 1}
