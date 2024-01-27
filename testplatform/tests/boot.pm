use Mojo::Base "basetest";
use testapi;

sub run() {
  assert_screen "bootloader", 400;
}

sub test_flags {
    # add milestone flag to save setup in lastgood VM snapshot
    return {fatal => 1, milestone => 1};
}

1;
