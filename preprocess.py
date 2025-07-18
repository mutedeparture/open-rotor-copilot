import pandas as pd
from datasets import Dataset

def load_and_prepare(csv_path="train.csv"):
    df = pd.read_csv(csv_path)


    dataset = Dataset.from_pandas(df)

    return dataset
