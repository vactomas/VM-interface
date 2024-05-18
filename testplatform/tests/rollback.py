from testapi import *


def run(self):
    assert_screen("rollback-test", 1)


def test_flags(self):
    return {"fatal": 0, "ignore_failure": 1}
