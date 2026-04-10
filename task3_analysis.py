import pandas as pd
import numpy as np
import os


# 1. LOAD AND EXPLORE DATA


file_path = "data/trends_clean.csv"

try:
    df = pd.read_csv(file_path)
    print(f"Loaded data: {df.shape}")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# -------------------------------
# 2. NUMPY ANALYSIS
# -------------------------------

scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score:.2f}")
print(f"Median score : {median_score:.2f}")
print(f"Std deviation: {std_score:.2f}")
print(f"Max score    : {max_score}")
print(f"Min score    : {min_score}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]

print(f"\nMost commented story:")
print(f"\"{max_comments_row['title']}\" — {max_comments_row['num_comments']} comments")

# -------------------------------
# 3. ADD NEW COLUMNS
# -------------------------------

# engagement = num_comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = score > average score
df["is_popular"] = df["score"] > avg_score

# -------------------------------
# 4. SAVE RESULT
# -------------------------------

output_file = "data/trends_analysed.csv"

# Ensure folder exists
if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")