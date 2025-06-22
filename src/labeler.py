import os

class Labeler:
    def __init__(self, input_txt_path: str, output_conll_path: str):
        self.input_txt_path = input_txt_path
        self.output_conll_path = output_conll_path

    def convert_to_conll(self):
        os.makedirs(os.path.dirname(self.output_conll_path), exist_ok=True)

        with open(self.input_txt_path, 'r', encoding='utf-8') as infile, \
             open(self.output_conll_path, 'w', encoding='utf-8') as outfile:

            for line in infile:
                line = line.strip()
                if not line:
                    outfile.write("\n")
                    continue
                parts = line.split()
                for part in parts:
                    label = "O"
                    if "/PRODUCT" in part:
                        token = part.replace("/PRODUCT", "")
                        label = "B-PRODUCT"
                    elif "/PRICE" in part:
                        token = part.replace("/PRICE", "")
                        label = "B-PRICE"
                    elif "/LOC" in part:
                        token = part.replace("/LOC", "")
                        label = "B-LOC"
                    else:
                        token = part
                    outfile.write(f"{token} {label}\n")
                outfile.write("\n")
