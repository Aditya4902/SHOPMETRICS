# ShopMetrics — E-Commerce Sales Analysis

> ShopMetrics is a retail analytics project that turns raw e-commerce order data into business insights using Python, SQL, and an interactive web dashboard.

E-Commerce sales analysis of 128K+ orders using Python (Pandas, NumPy) and SQL — with KPI dashboard, cohort retention, CLV segmentation & interactive visualizations.

---

## One-Line Summary
Analysed 128K+ retail orders to uncover revenue trends, customer segments, and category performance using Python and advanced SQL. Built cohort retention analysis, CLV segmentation with window functions (RANK, LAG, NTILE), and an interactive dashboard deployed on GitHub Pages. Key finding: VIP customers (top 25%) drive 52% of revenue with 18.4% YoY growth.

---

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

---

## Key Findings
- 18.4% YoY revenue growth driven by Electronics (+21%) and Beauty (+20%)
- Q4 (Oct–Dec) accounts for 38% of annual revenue — festive season effect
- VIP customers (top 25%) contribute 52% of total revenue
- Return rate dropped from 2.5% → 2.1%, saving ~₹18L in logistics cost
- Sunday is the lowest order day — 11% below weekly average

---

## Tech Stack
| Tool | Usage |
|------|-------|
| Python · Pandas | EDA, feature engineering, cohort analysis |
| Python · NumPy | Statistical analysis, outlier detection |
| SQL (MySQL) | Revenue queries, window functions, CLV segmentation |
| Chart.js | Interactive visualizations |
| HTML / CSS / JS | Dashboard UI |

---

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

---

## Resume Bullet Points
- Analysed 128K+ e-commerce orders using Pandas & NumPy to surface revenue trends and customer segmentation insights
- Wrote advanced SQL queries (window functions: RANK, LAG, NTILE) to compute Customer Lifetime Value and product rankings
- Built cohort retention analysis identifying a 68% customer retention rate and VIP segment contributing 52% of revenue
- Identified ₹18L cost-saving opportunity through return rate reduction from 2.5% to 2.1%
- Deployed interactive data dashboard on GitHub Pages with Chart.js visualisations

---

## Interview Pitch
> "I built ShopMetrics — an end-to-end e-commerce analysis using Python and SQL on 128K orders. I did cohort analysis, CLV segmentation using SQL window functions, and deployed an interactive dashboard on GitHub Pages."

---

## Live Demo
https://aditya4902.github.io/SHOPMETRICS/

## Author
Aditya Kumar Shah · (https://www.linkedin.com/in/aditya-kumar-shah-7383bb2a7?utm_source=share_via&utm_content=profile&utm_medium=member_ios)· [GitHub] https://github.com/Aditya4902

---

*ShopMetrics · Portfolio Data Project · FY 2023 · #python #pandas #sql #data-analysis #ecommerce #chartjs*
