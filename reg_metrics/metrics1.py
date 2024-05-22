# Многие библиотеки уже содержат эти метрики.
# Но в этом задании вам необходимо будет реализовать функции для расчета этих метрик самостоятельно.
# Напишите функции для расчета:
# MSE
# RMSE
# MAE
# MAPE
# R2

import numpy as np

def mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Вычисляет среднеквадратичную ошибку."""
    return np.mean((actual - predicted)**2)

def root_mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Вычисляет корень из среднеквадратичной ошибки."""
    return np.mean((actual - predicted)**2) ** 0.5

def mean_absolute_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Вычисляет среднюю абсолютную ошибку."""
    return np.mean(np.abs(actual - predicted))

def mean_absolute_percentage_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Вычисляет среднюю абсолютную процентную ошибку."""
    return np.mean(np.abs((actual - predicted) / actual)) * 100

def r_squared(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Вычисляет коэффициент детерминации (R-квадрат)."""
    return 1 - np.mean((actual - predicted)**2) / np.mean((actual - np.mean(actual))**2)
