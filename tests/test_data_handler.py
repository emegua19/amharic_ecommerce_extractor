import pytest
from src.data_handler import DataHandler

def test_handler_initialization():
    handler = DataHandler("config.yaml")
    assert handler.api_id is not None
    assert handler.channels

def test_fetch_mock(monkeypatch):
    handler = DataHandler("config.yaml")
    monkeypatch.setattr(handler, "fetch_messages", lambda limit=10: [{"msg": "test"}])
    df = handler.fetch_messages()
    assert isinstance(df, list) or len(df) > 0
