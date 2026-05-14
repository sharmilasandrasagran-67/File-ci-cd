import pandas as pd

def remove_duplicates(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Load a CSV file, remove duplicate rows, and save the cleaned dataset.

    Parameters:
        input_path (str): Path to the input CSV file.
        output_path (str): Path to save the cleaned CSV file.

    Returns:
        pd.DataFrame: The cleaned DataFrame without duplicates.
    """
    # Load dataset
    df = pd.read_csv(input_path)

    # Remove duplicate rows
    df_cleaned = df.drop_duplicates()

    # Save cleaned dataset
    df_cleaned.to_csv(output_path, index=False)

    print(f"Duplicate rows removed successfully. Cleaned file saved to {output_path}")
    return df_cleaned


# Allow script execution directly (not just import)
if __name__ == "__main__":
    input_file = "data/dataset1.csv"
    output_file = "data/processed_dataset.csv"
    remove_duplicates(input_file, output_file)
