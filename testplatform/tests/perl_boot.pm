package boot;

use base 'basetest';

use testapi;
use utils;

sub run {

  sleep 2;
  uefi_boot;
  #send_key "up";
  #send_key "ret";

  sleep 600;

  #select_console "tty3-console";
  
  console_login;

  sleep 10;

  type_string "plasmashell\n";
  sleep 20;
  #desktop_vt;

  # Wait for bootloader to appear
  assert_screen "boot", 20;

  # Press ENTER to boot right away
  type_string("opensuse");
  send_key "ret";

  # Check if booted to desktop
  assert_screen "desktop", 400;
}

sub test_flags {
    # add milestone flag to save setup in lastgood VM snapshot
    return {milestone => 1};
}

1;
