import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    '''Calculate sMAPE for two arrays'''
    abs_diff = np.abs(y_true - y_pred)
    abs_sum = np.abs(y_true) + np.abs(y_pred)
    inv_denom = np.where(abs_sum == 0, 1, abs_sum / 2)
    return np.mean(abs_diff / inv_denom)
