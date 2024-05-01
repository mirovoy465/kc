-- В таблице new_payments хранится информация о пользователях и о том, какие курсы они покупали.  Подробная структура таблицы описана на вкладке Структура данных.

-- Колонки в ожидаемой таблице:
-- time — месяц агрегации в формате DD/MM/YY - например, 01/12/19
-- mode — тип оплаты
-- percents — процент успешных оплат за месяц по данному типу

-- Необходимо отсортировать по возрастанию времени,  а также возрастанием типа оплаты по алфавиту (ApplePay, GooglePay и т.д.). 
-- Не рассматривать транзакции, где способ оплаты не определен («Не определено»).

SELECT
    CAST(DATE_TRUNC('month', date) AS DATE) as time,
    mode,
    (COUNT(CASE WHEN status = 'Confirmed' THEN 1 END) * 100.0) / COUNT(*) AS percents
FROM new_payments
WHERE mode <> 'Не определено'
GROUP BY date_trunc('month', date), mode
ORDER BY date_trunc('month', date) ASC, mode;
