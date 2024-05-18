from testapi import *
from utilities import open_app


def run(self):
    url = get_var("URL_WEB_APP")
    send_key("super")
    sleep(2)
    type_string(f"firefox {url}\n")
    assert_screen("firefox_open", 50)
    assert_and_click("firefox_open")
    assert_screen("next_slide", 10)
    assert_and_click("next_slide")
    assert_screen("presentation", 10)


def test_flags(self):
    return {"fatal": 1}
