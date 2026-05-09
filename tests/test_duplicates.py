import pandas as pd

def test_duplicates_removed():

    # Load processed dataset
    df = pd.read_csv("data/processed_dataset.csv")

    # Count duplicate rows
    duplicate_count = df.duplicated().sum()

    # Test should pass if duplicates = 0
    assert duplicate_count == 0
