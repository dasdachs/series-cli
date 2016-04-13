import os
import sys

from series.base import main, get_data


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


def test_get_data():
    """
    This is the only "live" test with a HTTP request. It is intended to test if
    the API is reponsive. All the following tests use a mock requests object.
    """
    name = get_data(name="ncis")  # Just a show, no specific reason
    url = get_data(
        url="http://api.tvmaze.com/episodes/185054"  # from the API docs
    )
    assert name["name"] == "NCIS", "The API might have changed"
    assert url["name"], "The API might have changed"


def test_with_data(monkeypatch):
    def mockreturn(dict):
        pass
