from testapi import *


def run(self):
    sleep(15)

    send_key("up")
    sleep(1)
    send_key("ret")

    assert_screen("boot", 15)

    download_and_open()
    test_calc()


def download_and_open():
    sleep(10)
    assert_screen("fedora_welcome", 2)
    assert_and_click("fedora_welcome")

    send_key("super")
    sleep(5)

    # Open Terminal
    open_app("Terminal")
    assert_screen("terminal_opened", 2)

    # Get variables from test settings
    app_name = get_var("APP")
    url = get_var("URL")

    # Download app
    type_string(f"wget {url}\n")
    sleep(15)

    # Untar
    type_string(f"tar -xf ./{app_name}")
    send_key("tab")
    send_key("ret")
    sleep(15)

    # Chmod +x
    type_string(f"chmod +x {app_name}")
    send_key("tab")
    send_key("ret")
    sleep(2)


def open_app(app_name):
    # Type the app name and press ENTER
    type_string(app_name)

    sleep(1)
    send_key("ret")


def test_calc():
    type_string("./numi-cli '1 + 15'\n")
    assert_screen("calculation_complete", 2)
    type_string("./numi-cli '0b0010110110 in decimal'\n")
    assert_screen("decimal", 2)


def test_flags(self):
    return {"fatal": 1}
