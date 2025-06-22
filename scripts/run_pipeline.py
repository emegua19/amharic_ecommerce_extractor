from src.data_handler import DataHandler
from src.labeler import Labeler
import pandas as pd

def main():
    print("Starting pipeline...")

    # Task 1: Fetch and preprocess messages
    handler = DataHandler()
    df = handler.fetch_messages(limit=100)
    handler.save_dataframe(df, "data/processed/preprocessed_data.csv")
    print("✅ Data ingestion complete.")

if __name__ == "__main__":
    main()
