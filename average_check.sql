-- Вам предоставлен доступ к таблице default.view_checks, в ней содержатся данные о покупках совершенных в нашем магазине.
-- Вам необходимо посчитать 2 метрики за каждый месяц:
-- средний чек пользователя 
-- медианный чек пользователя

select
    DATE_TRUNC('month', buy_date) as month,
    AVG(check_amount) as avg_check,
    quantileExactExclusive (0.5) (check_amount) as median_check
from
    default.view_checks
group by
    month
order by
    month