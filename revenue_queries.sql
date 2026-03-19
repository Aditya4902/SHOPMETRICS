-- ── ShopMetrics · Revenue Queries · revenue_queries.sql ─────────────────────

-- Monthly Revenue & Growth Rate
SELECT
    DATE_FORMAT(order_date, '%Y-%m')        AS month,
    COUNT(DISTINCT order_id)                AS total_orders,
    ROUND(SUM(revenue), 2)                  AS total_revenue,
    ROUND(AVG(revenue), 2)                  AS avg_order_value,
    COUNT(DISTINCT customer_id)             AS unique_customers
FROM orders
WHERE order_status = 'completed'
  AND YEAR(order_date) = 2023
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

-- Top 10 Products by Revenue
SELECT
    p.product_name,
    p.category,
    COUNT(o.order_id)         AS total_orders,
    ROUND(SUM(o.revenue), 2)  AS total_revenue,
    ROUND(AVG(o.rating), 2)   AS avg_rating
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_status = 'completed'
GROUP BY p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- Category Revenue Share
SELECT
    category,
    ROUND(SUM(revenue), 2)                                       AS revenue,
    ROUND(SUM(revenue) * 100.0 / SUM(SUM(revenue)) OVER(), 2)   AS pct_share
FROM orders
GROUP BY category
ORDER BY revenue DESC;
