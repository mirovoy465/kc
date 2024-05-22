# Два месяца назад ваш коллега во время своей стажировки написал sMAPE, 
# который корректно работал в продакшене всё это время, однако периодически метрика выдаёт ошибку, 
# а вы теряете информацию. К сожалению, логи ошибки нам недоступны.
# Вы взялись помочь исправить случаи, когда данный код выдаёт ошибку, и исправить функцию, 
# если она вызывает ошибки, не меняя поведение метрики в остальных ситуациях.
# Гарантируется, что y_true и y_pred – одинаковой длины.

import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    '''Calculate sMAPE for two arrays'''
    abs_diff = np.abs(y_true - y_pred)
    abs_sum = np.abs(y_true) + np.abs(y_pred)
    inv_denom = np.where(abs_sum == 0, 1, abs_sum / 2)
    return np.mean(abs_diff / inv_denom)
