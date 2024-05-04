-- Вам необходимо рассчитать 2 метрики за каждый месяц:  ARPPU и AOV. В расчете используйте только данные со статусом Confirmed (подтверждено).

-- Колонки в ожидаемой таблице:
-- time – месяц агрегации в формате DD/MM/YY - например, 01/12/19
-- arppu 
-- aov 

select 
    date_trunc('month', date)::DATE as time,
    sum(amount)/count(distinct email_id) as arppu,
    avg(amount) as aov
from new_payments
where status = 'Confirmed'
group by time