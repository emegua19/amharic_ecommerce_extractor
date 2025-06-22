import pytest
from src.labeler import Labeler

def test_convert_to_conll():
    labeler = Labeler()
    labeler.convert_to_conll("data/processed/labeled_telegram_product_price_location.txt", "test_output.conll")
    with open("test_output.conll", "r") as f:
        assert len(f.readlines()) > 0