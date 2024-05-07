-- Вам предоставлен доступ к таблице sku_dict_another_one.
-- Напишите запрос и постройте дашборд в Redash с демонстрацией TOP-10 вендоров (колонка vendor),
-- которые имеют больше всего брендов (колонка brand) среди продаваемых SKU.
-- Таблица на выходе имеет два столбца vendor и brand:
select
    vendor,
    COUNT(distinct brand) as brand
from
    sku_dict_another_one
group by
    vendor
order by
    brand desc
LIMIT
    10