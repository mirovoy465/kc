select
    sku,
    dates,
    price,
    COUNT(sku) as qty
from
    transactions
group by
    dates,
    price,
    sku
order by
    sku