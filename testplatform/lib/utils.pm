package utils;

use base Exporter;
use Exporter;

use strict;
use testapi qw(is_serial_terminal :DEFAULT);

our @EXPORT = qw(
  console_login
  desktop_vt
  uefi_boot
);


# Handle console login
sub console_login {
  
  # Default credentials
  my %args = (
    user => "root",
    password => "",
    @_
  );
  
  # Handle login
  type_string $args{user};
  type_string "\n";

  #wait_serial("Password:", timeout => 2, quiet => 1);
  #type_string $args{password};
  type_string "\n";

  sleep 10;

  # Simple test
  #assert_script_run "id -un";
  #unless (wait_serial $args{user}, timeout => 5) {
  #  die "Login failed.";
  #};
};

# Figure out what tty the desktop is on, switch to it. Assumes we're
# at a root console
#
# From Fedora repo
sub desktop_vt {
    my $xout;
    # don't fail test if we don't find any process, just guess tty1.
    # os-autoinst calls the script with 'bash -e' which causes it to
    # stop as soon as any command fails, so we use ||: to make the
    # first grep return 0 even if it matches nothing
    eval { $xout = script_output ' loginctl | grep test ||:; ps -e | egrep "(startplasma|gnome-session|Xwayland|Xorg)" | grep -o "tty[0-9]" ||:' };
    #eval { $xout = script_output ' ps -e | egrep "(startplasma|gnome-session|Xwayland|Xorg)" | grep -o "tty[0-9]" ||:' };
    type_string $xout;
    type_string "\n";
    my $tty = 1;    # default
    while ($xout =~ /tty(\d)/g) {
        $tty = $1;    # most recent match is probably best
    }
    select_console "tty${tty}-console";
};

sub uefi_boot {
  # Enter GRUB2 edit mode
  send_key "e";
  
  # Scroll to gfxpayload and delete keep
  for (1 .. 2) { send_key "down"; }
  send_key "end";
  for (1 .. 4) { send_key "backspace"; }
  
  # Hardcode resolution 1024x768
  type_string "1024x768";

  send_key "home";

  # Set boot params
  for (1 .. 3) { send_key "down"; }
  send_key "ret";
  send_key "up";
  type_string "    Y2DEBUG=1 vga=791 video=1024x768 plymouth.ignore-serial-consoles console=ttyS0 console=tty linuxrc.log=/dev/ttyS0 linuxrc.core=/dev/ttyS0 linuxrc.debug=4,trace reboot_timeout=0 kernel.softlockup_panic=1";
  
  # Boot
  send_key "ctrl-x";
};

1;
