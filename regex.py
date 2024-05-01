# Задача
# Два месяца назад ваш коллега во время своей стажировки написал sMAPE, который корректно работал в продакшене всё это время,
# однако периодически метрика выдаёт ошибку, а вы теряете информацию. К сожалению, логи ошибки нам недоступны.

# import numpy as np

# def smape(y_true: np.array, y_pred: np.array) -> float:
#     return np.mean(2 * np.abs(y_true - y_pred) / (np.abs(y_true) + np.abs(y_pred)))

# Вы взялись помочь исправить случаи, когда данный код выдаёт ошибку, и исправить функцию, 
# если она вызывает ошибки, не меняя поведение метрики в остальных ситуациях.

import re
from typing import List

VALID_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    def is_valid_email(email: str) -> bool:
        return bool(VALID_EMAIL_PATTERN.fullmatch(email))
    
    return [email for email in strings if is_valid_email(email)]
