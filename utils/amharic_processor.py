import re

class AmharicProcessor:
    def __init__(self):
        self.punctuation_pattern = re.compile(r"[፣፡።!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]")

    def normalize(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text)  # remove extra whitespace
        text = self.punctuation_pattern.sub("", text)
        return text.strip()

    def tokenize(self, text: str) -> list:
        return text.split()

    def preprocess(self, text: str) -> str:
        normalized = self.normalize(text)
        tokens = self.tokenize(normalized)
        return ",".join(tokens)
