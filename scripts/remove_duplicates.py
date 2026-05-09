import pandas as pd

# Load dataset
df = pd.read_csv("data/sample_dataset.csv")

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Save cleaned dataset
df_cleaned.to_csv("data/processed_dataset.csv", index=False)

print("Duplicates removed successfully.")
