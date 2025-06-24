import os
import pytest
import pandas as pd
from unittest.mock import MagicMock
from src.data_handler import DataHandler


@pytest.fixture
def sample_config(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("""
telegram:
  session_name: "test_session"
  api_id: 123456
  api_hash: "test_hash"
channels:
  - "@TestChannel"
""")
    return str(config_path)


@pytest.fixture
def fake_messages():
    return [
        {
            "channel": "@TestChannel",
            "original_message": "አዲስ ሽማግሌ ቀሚስ በ200 ብር",
            "tokens": "አዲስ,ሽማግሌ,ቀሚስ,በ200,ብር",
            "views": 123,
            "timestamp": "2025-06-21T12:00:00"
        }
    ]


def test_init_handler(sample_config):
    handler = DataHandler(config_path=sample_config)
    assert handler.api_id == 123456
    assert handler.api_hash == "test_hash"
    assert handler.channels == ["@TestChannel"]
    assert handler.session == "test_session"


def test_fetch_messages_mocked(mocker, sample_config, fake_messages):
    handler = DataHandler(config_path=sample_config)

    # Mock Telethon client methods
    mocker.patch.object(handler.client, "start", return_value=None)
    mocker.patch.object(handler.client, "disconnect", return_value=None)
    mocker.patch.object(handler.processor, "preprocess", return_value="mocked,tokenized,text")

    # Simulate iter_messages returning mock message object
    message_mock = MagicMock()
    message_mock.message = "Mocked message"
    message_mock.views = 123
    message_mock.date = "2025-06-21T12:00:00"
    mocker.patch.object(handler.client, "iter_messages", return_value=[message_mock])

    df = handler.fetch_messages(limit=1)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "tokens" in df.columns
    assert df["tokens"].iloc[0] == "mocked,tokenized,text"


def test_save_to_csv(tmp_path, sample_config, fake_messages):
    handler = DataHandler(config_path=sample_config)
    df = pd.DataFrame(fake_messages)
    out_path = tmp_path / "test_output.csv"

    handler.save_to_csv(df, str(out_path))

    assert out_path.exists()
    saved_df = pd.read_csv(out_path)
    assert saved_df.shape[0] == 1
    assert saved_df.iloc[0]["tokens"] == "አዲስ,ሽማግሌ,ቀሚስ,በ200,ብር"
