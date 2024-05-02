-- Шаг 1. Вам даны данные о продажах товаров. Напишите запрос к таблице transactions в базе Simulator ML в Redash и получите следующие агрегированные данные:

-- sku — уникальный идентификатор товара.
-- dates — уникальный день.
-- price — средняя цена для товара-дня.
-- qty — суммарное кол-во покупок.


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