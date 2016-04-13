""" Testing the mock data generation """
import pytest

from tests import data


class TestDataGeneration:
    """
    Tests if the mock data function correctly returns the
    hardcoded examples.
    """
    def test_data_for_series(self):
        assert data.mock_get_data("series") == data.SERIES
    
    def test_data_for_previousepisode(self):
        assert data.mock_get_data("previousepisode") == data.PREV
    
    def test_data_for_nextepisode(self):
        assert data.mock_get_data("nextepisode") == data.NEXT


class TestDataChange:
    """
    Test if the chages to the return dict return the correct value.
    """
    change = {"name": None}
    wrong_key = {"dasDachs": "Poorly spelled badger in german."}

    def test_series_data_change(self):
        assert data.mock_get_data("series", **self.change)["name"] == None
    
    def test_prev_episode_data_change(self):
        assert data.mock_get_data("previousepisode", **self.change)["name"] == None
    
    def test_next_episode_data_change(self):
        assert data.mock_get_data("nextepisode", **self.change)["name"] == None
    
    def test_series_data_wrong_key(self):
        with pytest.raises(KeyError):
            data.mock_get_data("series", **self.wrong_key)["dasDachs"]
    
    def test_prev_episode_data_wrong_key(self):
        with pytest.raises(KeyError):
            data.mock_get_data("previousepisode", **self.wrong_key)["dasDachs"]
    
    def test_next_episode_data_wrong_key(self):
        with pytest.raises(KeyError):
            data.mock_get_data("nextepisode", **self.wrong_key)["dasDachs"]
