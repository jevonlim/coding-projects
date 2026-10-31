import pandas as pd
from pathlib import Path

def load_file(path):
    rows = []
    with open(path, encoding="latin-1") as f:
        for line in f:
            line = line.strip()
            if "@" in line:
                text, label = line.rsplit("@", 1)
                rows.append((text, label))

    return pd.DataFrame(rows, columns=["text", "label"])

data_dir = Path("data/FinancialPhraseBank-v1.0")
file_paths = sorted(data_dir.glob("Sentences_*Agree.txt"))
dfs = {}


for path in file_paths:
    name = path.stem.replace("Sentences_", "")
    dfs[name] = load_file(path)

df = dfs["50Agree"]
print(df["label"].value_counts())
print(df.sample(5, random_state=1))

