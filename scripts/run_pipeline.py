import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_handler import DataHandler
from src.labeler import Labeler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting data ingestion and labeling pipeline...")

    try:
        # Initialize DataHandler
        handler = DataHandler(config_path="config.yaml")
        
        # Fetch and save preprocessed data
        df = handler.fetch_messages(limit=100)
        handler.save_to_csv(df, "data/processed/preprocessed_data.csv")
        logging.info("Data saved to data/processed/preprocessed_data.csv")

        # Initialize Labeler and label a subset of data
        labeler = Labeler(output_dir="data/processed")
        # Take first 50 unique rows for labeling to avoid repetition
        sample_data = df.drop_duplicates(subset=["tokens"]).head(50).to_dict('records')
        labeled_data = labeler.label_dataset(sample_data)
        labeler.save_conll(labeled_data, "labeled_data.conll")
        logging.info("Labeled data saved to data/processed/labeled_data.conll")

        # Print sample of labeled data with message separation
        with open("data/processed/labeled_data.conll", encoding="utf-8") as f:
            content = f.read().split("\n\n")  # Split by blank lines
        print("\n--- Sample Labeled Data (CoNLL Format) ---\n")
        for i, msg in enumerate(content[:3], 1):  # Show first 3 messages
            print(f"Message {i}:\n{msg}\n")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()