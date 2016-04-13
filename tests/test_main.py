"""Tests the main function in base"""
from series import base
from tests.data import mock_get_data


class TestFullData:
    """
    Simulates a scenario were all data is retrived.
    TODO: implement it
    """
    def test_with_data(self, monkeypatch, capsys):
        def mockreturn(name):
            return mock_get_data("series")
        monkeypatch.setattr(base, "get_data", mockreturn)
