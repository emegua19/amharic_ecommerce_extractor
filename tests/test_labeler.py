import os
import pytest
import pandas as pd
from src.labeler import Labeler

@pytest.fixture
def sample_data():
    return [
        {"tokens": "💥,ሽማግሌ,ቀሚስ,በ,200,ብር,አዲስ,አበባ"},
        {"tokens": "🎯,LCD,ዋጋ,550,ብር,ቦሌ"}
    ]

def test_init_labeler(tmp_path):
    labeler = Labeler(output_dir=str(tmp_path))
    assert os.path.exists(str(tmp_path))
    assert labeler.output_dir == str(tmp_path)

def test_label_dataset(sample_data):
    labeler = Labeler()
    labeled_data = labeler.label_dataset(sample_data)
    assert len(labeled_data) == 2  # Two messages
    assert len(labeled_data[0]) > 0  # Non-empty sentences
    # Check for expected entity types
    labels = [label for sentence in labeled_data for _, label in sentence]
    assert "B-Product" in labels
    assert "I-Product" in labels
    assert "B-LOC" in labels
    assert "I-LOC" in labels
    assert "B-PRICE" in labels
    assert "I-PRICE" in labels
    assert "O" in labels

def test_save_conll(tmp_path, sample_data):
    labeler = Labeler(output_dir=str(tmp_path))
    labeled_data = labeler.label_dataset(sample_data)
    filepath = labeler.save_conll(labeled_data, "test_output.conll")
    assert os.path.exists(filepath)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    assert "B-Product" in content
    assert "\n\n" in content  # Check for message separation