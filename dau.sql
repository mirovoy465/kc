-- Вам предоставлен доступ к таблице default.churn_submits. В ней находятся данные по активности пользователей нашего Симулятора. 
-- Одна строка = одна попытка решения каким-то студентом какой-то задачи. 
-- 1. Напишите запрос с расчётом DAU на каждый день.
-- 2. Название столбцов должно быть day и dau (должны идти именно в таком порядке).
select
    DATE_TRUNC('day', timestamp)::DATE as day,
    COUNT(distinct user_id) as dau
from
    default.churn_submits
group by
    day
order by
    day