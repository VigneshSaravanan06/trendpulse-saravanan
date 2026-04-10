import pandas as pd
import os

# File path (make sure your JSON file exists here)
file_path = "data/trends_20260410.json"  

# 1. LOAD JSON FILE
try:
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from {file_path}")
except Exception as e:
    print("Error loading JSON:", e)
    exit()


# 2. CLEAN THE DATA

# Remove duplicates based on post_id
before = len(df)
df = df.drop_duplicates(subset=["post_id"])
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert score and num_comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra whitespace from title
df["title"] = df["title"].str.strip()

# 3. SAVE AS CSV
# -------------------------------

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# -------------------------------
# SUMMARY
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())