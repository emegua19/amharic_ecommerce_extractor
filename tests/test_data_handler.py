import pytest
from src.data_handler import DataHandler

def test_scrape_channels(mocker):
    handler = DataHandler()
    mocker.patch.object(handler.client, 'iter_messages', return_value=[{"text": "test"}])
    messages = handler.scrape_channels()
    assert len(messages) > 0