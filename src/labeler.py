import os
import logging
from typing import List, Tuple, Dict  # Added missing import

class Labeler:
    def __init__(self, output_dir: str = "data/processed"):
        """Initialize Labeler with output directory."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # Expanded location keywords
        self.location_keywords = {
            "አዲስ አበባ", "አዲስ", "ቦሌ", "መቀሌ", "መገናኛ", "ቢሮ", "ጣይቶ"
        }

    def label_dataset(self, data: List[Dict]) -> List[List[Tuple[str, str]]]:
        """
        Label preprocessed data into (token, label) tuples.

        Args:
            data (List[Dict]): List of dictionaries from preprocessed DataFrame (e.g., {'tokens': 'token1,token2'}).

        Returns:
            List[List[Tuple[str, str]]]: Labeled sentences.
        """
        labeled_data = []
        for item in data[:50]:  # Limit to 50 unique messages
            tokens = item.get("tokens", "").split(",")
            sentence = []
            prev_label = "O"
            for i, token in enumerate(tokens):
                token = token.strip()
                if not token or token in ["👍", "🎯", "💥", "🖌", "እና", "በ", "ለ", "ነው", "ያለው"]:
                    label = "O"
                elif token.isdigit() or "ብር" in token or "ዋጋ" in token or token in ["0902660722", "0928460606"]:
                    label = "B-PRICE" if i == 0 or prev_label not in ["B-PRICE", "I-PRICE"] else "I-PRICE"
                elif any(loc in token or token in loc for loc in self.location_keywords):
                    label = "B-LOC" if i == 0 or prev_label not in ["B-LOC", "I-LOC"] else "I-LOC"
                else:
                    label = "B-Product" if prev_label.startswith("O") else "I-Product"
                sentence.append((token, label))
                prev_label = label
            if sentence:
                labeled_data.append(sentence)
        self.logger.info(f"Labeled {len(labeled_data)} out of 50 messages.")
        return labeled_data

    def save_conll(self, labeled_data: List[List[Tuple[str, str]]], filename: str) -> str:
        """
        Save labeled data to CoNLL format.

        Args:
            labeled_data (List[List[Tuple[str, str]]]): List of sentences, each a list of (token, label) tuples.
            filename (str): Output file name.

        Returns:
            str: Full filepath of the saved file.
        """
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                for sentence in labeled_data:
                    if not sentence:
                        continue
                    for token, label in sentence:
                        f.write(f"{token} {label}\n")
                    f.write("\n")  # Sentence separator
            self.logger.info(f"Successfully saved labeled data to {filepath}")
            return filepath
        except IOError as e:
            self.logger.error(f"Failed to save CoNLL file: {str(e)}")
            raise