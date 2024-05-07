-- Вам предоставлен доступ к таблице sku_dict_another_one.
-- Напишите запрос и постройте дашборд в Redash с демонстрацией TOP-10 вендоров (колонка vendor), 
-- которые продают больше всего SKU (колонка sku_type).
-- Таблица на выходе имеет два столбца vendor и sku:
select
    vendor,
    COUNT(sku_type) as sku
from
    sku_dict_another_one
group by
    vendor
order by
    sku desc
LIMIT
    10