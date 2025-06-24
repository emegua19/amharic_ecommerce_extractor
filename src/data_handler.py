import os
import yaml
import pandas as pd
from telethon.sync import TelegramClient
from utils.amharic_processor import AmharicProcessor


class DataHandler:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        self.api_id = self.config["telegram"]["api_id"]
        self.api_hash = self.config["telegram"]["api_hash"]
        self.session = self.config["telegram"]["session_name"]
        self.channels = self.config["channels"]
        self.processor = AmharicProcessor()
        self.client = TelegramClient(self.session, self.api_id, self.api_hash)

    def fetch_messages(self, limit=100) -> pd.DataFrame:
        self.client.start()
        data = []

        for channel in self.channels:
            try:
                for message in self.client.iter_messages(channel, limit=limit):
                    if message.message:
                        clean_tokens = self.processor.preprocess(message.message)
                        data.append({
                            "channel": channel,
                            "original_message": message.message,
                            "tokens": clean_tokens,
                            "views": message.views,
                            "timestamp": message.date,
                        })
            except Exception as e:
                print(f"[ERROR] Failed to fetch from {channel}: {e}")

        self.client.disconnect()
        return pd.DataFrame(data)

    def save_to_csv(self, df: pd.DataFrame, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8")
