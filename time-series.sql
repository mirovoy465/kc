-- В этой задаче необходимо построить дашборд с временным рядом суммы оплат за неделю. 
-- На оси X - неделя, на оси Y - сумма (не количество) всех успешных оплат за неделю.

-- Колонки в ожидаемой таблице:
-- weeks  - неделя агрегации в формате DD/MM/YY - например, 02/12/19
-- sum_receipt - сумма оплат за неделю

select
    date_trunc('week', date)::DATE as weeks,
    sum(amount) as sum_receipt
from new_payments
where status = 'Confirmed'
group by weeks
order by weeks