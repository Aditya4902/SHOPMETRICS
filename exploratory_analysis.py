# ── ShopMetrics · E-Commerce Sales Analysis · exploratory_analysis.py ──────
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("ecommerce_orders.csv", parse_dates=["order_date"])
print(df.shape)        # (128000, 14)
print(df.dtypes)

# ── Feature Engineering ──────────────────────────────────────────────────────
df["month"]    = df["order_date"].dt.to_period("M")
df["weekday"]  = df["order_date"].dt.day_name()
df["quarter"]  = df["order_date"].dt.quarter

# ── Monthly Revenue ───────────────────────────────────────────────────────────
monthly_rev = (
    df.groupby("month")["revenue"]
      .agg(["sum", "mean", "count"])
      .rename(columns={"sum": "total_rev", "mean": "aov", "count": "orders"})
      .reset_index()
)
print("\nMonthly Revenue:\n", monthly_rev)

# ── Category Performance ──────────────────────────────────────────────────────
cat_perf = (
    df.groupby("category")
      .agg(total_rev=("revenue", "sum"),
           orders    =("order_id", "nunique"),
           avg_rating=("rating",  "mean"))
      .sort_values("total_rev", ascending=False)
)
print("\nCategory Performance:\n", cat_perf)

# ── Cohort Retention ──────────────────────────────────────────────────────────
df["cohort"]        = df.groupby("customer_id")["order_date"].transform("min")
df["cohort_month"]  = df["cohort"].dt.to_period("M")
df["period_number"] = (
    (df["month"] - df["cohort_month"]).apply(lambda x: x.n)
)
cohort_data = df.groupby(["cohort_month", "period_number"])["customer_id"].nunique()
print("\nCohort Data:\n", cohort_data)

# ── Statistical Summary ───────────────────────────────────────────────────────
print("\nRevenue Stats:\n", df["revenue"].describe())
print("Skewness:", np.round(df["revenue"].skew(), 3))
print("Correlation matrix:\n", df[["revenue", "discount", "rating"]].corr())
