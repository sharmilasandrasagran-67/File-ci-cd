import pandas as pd

# Load dataset
df = pd.read_csv("data/dataset1.csv")

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save cleaned dataset
df_cleaned.to_csv("data/processed_dataset.csv", index=False)

print("Duplicate rows removed successfully.")
