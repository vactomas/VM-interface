from testapi import *

def run(self):

    send_key("super")
    sleep(6)
    type_string("edge")
    sleep(2)
    send_key("ret")
    assert_screen("win_edge", 20)

def test_flags(self):
    return {'fatal': 1}

