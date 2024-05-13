-- Сделаем выгрузку датасета с кредитными заявками. 
select
    age,
    income,
    dependents,
    has_property,
    has_car,
    credit_score,
    job_tenure,
    has_education,
    loan_amount,
    TIMESTAMPDIFF (DAY, loan_start, loan_deadline) as loan_period,
    GREATEST(TIMESTAMPDIFF (DAY, loan_deadline, loan_payed), 0) as delay_days
from
    default.loan_delay_days
order by
    id