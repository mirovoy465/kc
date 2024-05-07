-- Вам предоставлен доступ к таблице sku_dict_another_one.
-- Напишите запрос и постройте дашборд в Redash с демонстрацией TOP-10 sku (колонка sku_type), 
-- которые имеют больше всего вендоров (колонка vendor), которые их продают.
-- Таблица на выходе имеет два столбца sku_type и count_vendor:
select
  sku_type,
  count(distinct vendor) as count_vendor
from
  sku_dict_another_one
group by
  sku_type
order by
  count_vendor desc
LIMIT
  10