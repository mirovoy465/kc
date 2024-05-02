select DISTINCT
    DATE(timestamp) as day,
    COUNT(DISTINCT user_id) OVER (
        order by
            DATE(timestamp) range between 6 preceding
            and current row
    ) as wau
from
    default.churn_submits
