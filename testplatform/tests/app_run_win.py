from testapi import *


def run(self):
    type_string(f"3+2=\n")
    assert_screen("qalculate_5_win", 1)
    assert_and_click("qalculate_5_win")
    assert_screen("qalculate_5plus_win", 1)
    assert_and_click("qalculate_5plus_win")
    assert_screen("qalculate_5plus5_win", 1)
    assert_and_click("qalculate_5plus5_win")
    assert_screen("qalculate_equals_win", 1)
    assert_and_click("qalculate_equals_win")
    assert_screen("qalculate_result_win", 1)


def test_flags(self):
    return {"fatal": 1}
