from src.data_handler import DataHandler
from src.labeler import Labeler
import pandas as pd

def main():
    print("Starting pipeline...")

    # Task 1: Fetch and preprocess messages
    handler = DataHandler()
    df = handler.fetch_messages(limit=100)
    handler.save_dataframe(df, "data/processed/preprocessed_data.csv")
    print("Data ingestion complete.")

    # Task 2: Convert labeled text to CoNLL
    labeler = Labeler(
        input_txt_path="data/processed/labeled_telegram_product_price_location.txt",
        output_conll_path="data/processed/labeled_data.conll"
    )
    labeler.convert_to_conll()
    print("Labeling to CoNLL format complete.")

if __name__ == "__main__":
    main()
