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
    type_string("    Y2DEBUG=1 vga=791 video=1024x768 plymouth.ignore-serial-consoles console=ttyS0 console=tty linuxrc.log=/dev/ttyS0 linuxrc.core=/dev/ttyS0 linuxrc.debug=4,trace reboot_timeout=0 kernel.softlockup_panic=1")
  
    # Boot
    send_key("ctrl-x")
