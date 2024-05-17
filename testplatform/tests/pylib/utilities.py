from testapi import *


def uefi_boot():
    # Enter GRUB2 edit mode
    send_key("e")

    # Scroll to gfxpayload and delete keep
    for i in range(2):
        send_key("down")

    send_key("end")

    for i in range(4):
        send_key("backspace")

    # Hardcode resolution 1024x768
    type_string("1024x768")

    send_key("home")

    # Set boot params
    for i in range(3):
        send_key("down")

    send_key("ret")
    send_key("up")
    type_string(
        "    Y2DEBUG=1 vga=791 video=1024x768 plymouth.ignore-serial-consoles console=ttyS0 console=tty linuxrc.log=/dev/ttyS0 linuxrc.core=/dev/ttyS0 linuxrc.debug=4,trace reboot_timeout=0 kernel.softlockup_panic=1"
    )

    # Boot
    send_key("ctrl-x")


def uefi_boot_arm():
    # Enter GRUB2 edit mode
    send_key("e")

    # Scroll to gfxpayload and delete keep
    for i in range(2):
        send_key("down")

    send_key("end")

    for i in range(4):
        send_key("backspace")

    # Hardcode resolution 1024x768
    type_string("1024x768")

    send_key("home")

    # Set boot params
    for i in range(3):
        send_key("down")

    send_key("ret")
    send_key("up")
    type_string(
        "    Y2DEBUG=1 plymouth.ignore-serial-consoles console=ttyAMA0 console=tty linuxrc.log=/dev/ttyAMA0 linuxrc.core=/dev/ttyAMA0 linuxrc.debug=4,trace reboot_timeout=0 kernel.softlockup_panic=1"
    )

    # Boot
    send_key("ctrl-x")


def open_app(app_name):
    # Open app menu
    send_key("super")

    # Sleep for a bit to ensure it opens
    sleep(1)

    # Type the app name and press ENTER
    type_string(app_name)

    sleep(1)
    send_key("ret")
    sleep(1)


def download_and_open_linux():
    # Get variables from test settings
    app_name = get_var("APP")
    url = get_var("URL")

    # Open Konsole
    open_app("Konsole")
    assert_screen("konsole_opened", 2)

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

    # Run app
    type_string(f"./{app_name}\n")
    sleep(1)


def download_and_open_windows():
    # Get variables from test settings
    app_name = get_var("APP")
    app_name_run = get_var("APP_RUN")
    url = get_var("URL")

    sleep(10)
    send_key("ret")
    sleep(10)

    # Open Konsole
    open_app("powershell")
    sleep(2)
    send_key("ret")
    sleep(2)
    send_key("f11")
    assert_screen("powershell-open", 10)

    # Download app
    type_string(f"wget {url} -o {app_name}.zip")
    sleep(2)
    send_key("ret")
    sleep(600)

    # Untar
    type_string(f"Expand-Archive {app_name}")
    sleep(1)
    send_key("tab")
    sleep(1)
    send_key("ret")
    sleep(30)

    # Open app folder
    type_string(f"cd {app_name}")
    sleep(1)
    send_key("ret")
    sleep(1)
    type_string(f"cd {app_name}")
    sleep(1)
    send_key("ret")

    # Run app
    sleep(1)
    type_string(f"./{app_name_run}")
    sleep(1)
    send_key("ret")
    sleep(10)

