import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust path
from src.data_handler import DataHandler
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info(" Starting data ingestion pipeline...")

    handler = DataHandler()
    df = handler.fetch_messages(limit=100)
    handler.save_to_csv(df, "data/processed/preprocessed_data.csv")

    logging.info(" Data saved to data/processed/preprocessed_data.csv")

if __name__ == "__main__":
    main()
