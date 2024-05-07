-- Вам предоставлен доступ к таблице sku_dict_another_one. 
-- Напишите запрос и постройте дашборд в Redash с демонстрацией TOP-10 брендов (колонка brand), 
-- которые имеют большее количество SKU (stock-keeping unit) — колонка sku_type. 
-- Таблица на выходе имеет два столбца brand и count_sku:
select
    brand,
    COUNT(sku_type) as count_sku
from sku_dict_another_one
where brand is not null
group by brand
order by count_sku desc
limit 10