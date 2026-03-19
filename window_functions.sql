-- ── ShopMetrics · Window Functions · window_functions.sql ───────────────────

-- Running Total & Rank per Customer
SELECT
    order_date,
    customer_id,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,

    RANK() OVER (
        PARTITION BY category
        ORDER BY revenue DESC
    ) AS rank_in_category,

    LAG(revenue, 1) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS prev_order_revenue,

    revenue - LAG(revenue, 1) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS revenue_change
FROM orders
WHERE order_status = 'completed';

-- Customer Lifetime Value (CLV) with Segmentation
WITH customer_stats AS (
    SELECT
        customer_id,
        COUNT(order_id)               AS total_orders,
        SUM(revenue)                  AS total_spent,
        DATEDIFF(MAX(order_date),
                 MIN(order_date))     AS customer_lifespan_days
    FROM orders
    GROUP BY customer_id
)
SELECT
    customer_id,
    total_orders,
    ROUND(total_spent, 2)                          AS clv,
    NTILE(4) OVER (ORDER BY total_spent DESC)      AS clv_quartile,
    CASE
        WHEN total_spent > 50000  THEN 'VIP'
        WHEN total_spent > 20000  THEN 'Premium'
        WHEN total_spent > 5000   THEN 'Regular'
        ELSE 'New'
    END AS segment
FROM customer_stats
ORDER BY clv DESC;
