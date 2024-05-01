# Вашей команде поручили заняться разработкой сервиса для автоматического отлова ботов и предотвращения DDoS-атак. 
# Для регистрации на сайте необходимо указать email-адрес. Не всегда указанный набор символов является корректным email.

# Вашему коллеге-стажёру поручили выполнить это маленькое задание, в результате чего был разработан код, приведённый ниже:

# import re
# from typing import List


# def valid_emails(strings: List[str]) -> List[str]:
#     """Take list of potential emails and returns only valid ones"""

#     valid_email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

#     def is_valid_email(email: str) -> bool:
#         return bool(re.fullmatch(valid_email_regex, email))

#     emails = []
#     for email in strings:
#         if is_valid_email(email):
#             emails.append(email)

#     return emails


# Код работает корректно и полностью решает задачу, но после ревью TeamLead`а остались комментарии о том,
# что его можно ускорить минимум в 2 раза, буквально поменяв две строчки, 
# а какие он не сказал – лишь оставил ссылку на страницу про регулярные выражения в Python в качестве подсказки. 

import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    '''Calculate sMAPE for two arrays'''
    abs_diff = np.abs(y_true - y_pred)
    abs_sum = np.abs(y_true) + np.abs(y_pred)
    inv_denom = np.where(abs_sum == 0, 1, abs_sum / 2)
    return np.mean(abs_diff / inv_denom)
