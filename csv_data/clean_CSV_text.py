import pandas as pd

# Load your CSV file
df = pd.read_csv("CNN_Articles_Dataset.csv")

# print(df.columns)

# Clean up the "body" column: remove all occurrences of â€™
df["Body"] = df["Body"].str.replace("â€™", "", regex=False)

# Drop any rows with null/missing values
df = df.dropna()

# Save the cleaned CSV
df.to_csv("CNN_articles_cleaned.csv", index=False)

print("✅ Cleaned CSV saved as articles_cleaned.csv")
