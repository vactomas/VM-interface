use testapi;
use autotest;
 
sub load_python_main() {

  autotest::loadtest "tests/main.py";

}

## Load main.py

load_python_main;

1;