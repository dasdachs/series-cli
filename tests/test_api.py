"""Test if TVMaze API returns the correct responses"""
from series.base import main, get_data
from tests.data import mock_get_data


def test_get_data():
    """
    This is the only "live" test with a HTTP request. It is intended to test if
    the API is reponsive. All the following tests use a mock requests object.
    """
    name = get_data(name="ncis")  # Just a show, no specific reason
    url = get_data(
        url="http://api.tvmaze.com/episodes/185054"  # from the API docs
    )
    api_fail_msg = "The API might have changed"
    # Asserts
    # =======
    # - the name key must exists, if not, the API has changed
    # - the _links key contains at least a key for self, which is the
    # the URL for the API endpoit, constructed with the ID of the item.
    # If there is no such key, the API must have changed.
    assert name["name"] == "NCIS", api_fail_msg
    assert name["_links"], api_fail_msg
    assert url["name"], api_fail_msg
    assert url["_links"], api_fail_msg
