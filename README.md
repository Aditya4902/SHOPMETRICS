# SHOPMETRICS
E-Commerce sales analysis of 128K+ orders using Python (Pandas, NumPy) and SQL — with KPI dashboard, cohort retention, CLV segmentation &amp; interactive visualizations.
# ShopMetrics — E-Commerce Sales Analysis

> Retail performance insights using Python & SQL · FY 2023

## Project Structure

```
shopmetrics/
├── index.html                  ← Interactive dashboard (open in browser)
├── exploratory_analysis.py     ← EDA: feature engineering, cohort analysis
├── data_cleaning.py            ← Data cleaning & preprocessing pipeline
├── revenue_queries.sql         ← SQL: monthly revenue, top products, category share
├── window_functions.sql        ← SQL: RANK, LAG, NTILE, running totals, CLV
└── README.md
```

## Key Findings
- 18.4% YoY revenue growth driven by Electronics (+21%) and Beauty (+20%)
- Q4 (Oct–Dec) accounts for 38% of annual revenue — festive season effect
- VIP customers (top 25%) contribute 52% of total revenue
- Return rate dropped from 2.5% → 2.1%, saving ~₹18L in logistics cost
- Sunday is the lowest order day — 11% below weekly average

## Tech Stack
| Tool | Usage |
|------|-------|
| Python · Pandas | EDA, feature engineering, cohort analysis |
| Python · NumPy | Statistical analysis, outlier detection |
| SQL (MySQL) | Revenue queries, window functions, CLV segmentation |
| Chart.js | Interactive visualizations |
| HTML / CSS / JS | Dashboard UI |

## How to Run

### Dashboard
Open `index.html` directly in any browser — no setup needed.

### Python scripts
```bash
pip install pandas numpy
python exploratory_analysis.py
python data_cleaning.py
```

### SQL queries
Run `revenue_queries.sql` and `window_functions.sql` in MySQL Workbench or any MySQL client against your orders database.


## Author
Your Name · [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)
