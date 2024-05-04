-- В таблице new_payments хранится информация о пользователях и покупках, которые они совершали. Таблица содержит следующие поля:
-- id - персональный номер транзакции
-- date - дата проведения транзакции
-- amount - сумма оплаты пользователем
-- status - статус оплаты (подтвержденные оплаты имеют статус "Confirmed")
-- mode - способ оплаты (Visa, MasterCard, ApplePay и др.)
-- email_id - уникальный id почты пользователя
-- phone_id - номер телефона пользователя, связан с email_id. Номера телефонов могут повторяться, либо отсутствовать вовсе.

-- Задание
-- В этой задаче необходимо сегментировать пользователей на основе данных из таблицы по оплате. 
-- Учитывается каждая оплата, вне зависимости от того, первичная она или повторная в рамках одного пользователя,
-- также учитываются только успешные оплаты, совершенные через банковскую карту ('MasterCard', 'МИР', 'Visa').

-- В ответ требуется загрузить файл SQL запроса, который возвращает колонки purchase_range и num_of_users.
-- Сегментацию по цене следует проводить с шагом 20 тыс. Нижняя граница текущего сегмента строго больше верхней границы предыдущего.
-- Оплаты, превышающие 100 тыс., объединить в одном сегменте. Верхняя граница для этого сегмента - это максимально возможная сумма среди всех пользователей.

WITH
    user_payments AS (
        SELECT
            email_id,
            SUM(amount) AS total_amount,
        FROM
            new_payments
        WHERE
            status = 'Confirmed'
            AND mode IN ('MasterCard', 'МИР', 'Visa')
        GROUP BY
            email_id
    ),
    segments_names as
    (
        select
            1 as segment,
            '0-20000' as purchase_range
        union all
        select
            2 ,
            '20000-40000'
        union all
        select
            3 ,
            '40000-60000'
        union all
        select
            4 ,
            '60000-80000'
        union all
        select
            5 ,
            '80000-100000'
        union all
        select
            6 ,
            '100000-' || max(total_amount)::int
        from user_payments
    ),
    segments as
    (
        select
            case
                when total_amount <= 20000 then 1
                when total_amount > 20000 and total_amount <= 40000 then 2
                when total_amount > 40000 and total_amount <= 60000 then 3
                when total_amount > 60000 and total_amount <= 80000 then 4
                when total_amount > 80000 and total_amount <= 100000 then 5
                when total_amount > 100000 then 6
            end as segment,
            count(email_id) as num_of_users
        from user_payments
        group by segment
        order by segment
    )
select
    purchase_range,
    num_of_users
from segments as s
join segments_names as sn on s.segment = sn.segment
