import re

class AmharicProcessor:
    def __init__(self):
        self.punct_pattern = re.compile(r"[፣፡።!\"#$%&'()*+,\-./:;<=>?@[\]^_`{|}~]")

    def normalize(self, text: str) -> str:
        """Remove unwanted punctuation and whitespace."""
        text = self.punct_pattern.sub("", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def tokenize(self, text: str) -> list:
        return text.split()

    def preprocess(self, text: str) -> str:
        """Full pipeline: normalize + tokenize → return comma-separated string."""
        normalized = self.normalize(text)
        tokens = self.tokenize(normalized)
        return ",".join(tokens)
