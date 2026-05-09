import pandas as pd

def test_duplicates_removed():
    df = pd.read_csv("data/processed_dataset.csv")

    # Check for duplicate rows
    duplicates = df.duplicated().sum()

    assert duplicates == 0
