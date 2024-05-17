from testapi import *


def run(self):
    type_string(f"3+2=\n")
    assert_screen("qalculate_5_linux", 1)
    assert_and_click("qalculate_5_linux")
    assert_screen("qalculate_5plus_linux", 1)
    assert_and_click("qalculate_5plus_linux")
    assert_screen("qalculate_5plus5_linux", 1)
    assert_and_click("qalculate_5plus5_linux")
    assert_screen("qalculate_equals_linux", 1)
    assert_and_click("qalculate_equals_linux")
    assert_screen("qalculate_result_linux", 1)


def test_flags(self):
    return {"fatal": 1}
