# ── ShopMetrics · Data Cleaning & Preprocessing · data_cleaning.py ──────────
import pandas as pd
import numpy as np

df = pd.read_csv("raw_orders.csv")

# 1. Check missing values
print(df.isnull().sum())
print(f"Missing: {df.isnull().sum().sum()} cells")

# 2. Drop duplicates
before = len(df)
df = df.drop_duplicates(subset=["order_id"])
print(f"Removed {before - len(df)} duplicate rows")

# 3. Fix data types
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["revenue"]    = pd.to_numeric(df["revenue"],    errors="coerce")

# 4. Handle outliers (IQR method)
Q1, Q3 = df["revenue"].quantile([0.25, 0.75])
IQR     = Q3 - Q1
df = df[
    (df["revenue"] >= Q1 - 1.5 * IQR) &
    (df["revenue"] <= Q3 + 1.5 * IQR)
]

# 5. Fill missing ratings with category median
df["rating"] = df.groupby("category")["rating"].transform(
    lambda x: x.fillna(x.median())
)

# 6. Standardize text fields
df["category"] = df["category"].str.strip().str.title()
df["city"]     = df["city"].str.strip().str.title()

print("✓ Clean dataset ready:", df.shape)
df.to_csv("clean_orders.csv", index=False)
