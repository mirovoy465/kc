from __future__ import annotations
import numpy as np

# Реализуйте две функции:
# mse – принимает на вход вектор значений, возвращает значение mse.
# weighted_mse – принимает на вход два вектора значений (слева и справа) и возвращает средневзвешенную mse.

def mse(y: np.ndarray) -> float:
    """Compute the mean squared error of a vector."""
    return np.mean((y - np.mean(y)) ** 2)


def weighted_mse(y_left: np.ndarray, y_right: np.ndarray) -> float:
    """Compute the weighted mean squared error of two vectors."""
    mse_l = mse(y_left)
    mse_r = mse(y_right)
    size_left = y_left.shape[0]
    size_right = y_right.shape[0]
    return (mse_l * size_left + mse_r * size_right)/(size_left + size_right)

# Реализуйте функцию split. 
# Функция принимает на вход выборку (матрицу признаков X и вектор целевой переменной y) и индекс признака.
# Возвращает значение порога с наилучшим разбиением.

def split(X: np.ndarray, y: np.ndarray, feature: int) -> float:
    """Find the best split for a node (one feature)"""
    thresholds = np.unique(X[:, feature])
    entropy_best = None
    threshold_best = None
    for threshold in thresholds:
        left = y[X[:, feature] <= threshold]
        right = y[X[:, feature] > threshold]
        if left.size == 0 or right.size == 0:
            continue
        entropy = weighted_mse(left, right)
        if entropy_best is None or entropy < entropy_best:
            entropy_best = entropy
            threshold_best = threshold
    return threshold_best, entropy_best

# Реализуйте функцию best_split. 
# Функция принимает на вход выборку (матрицу признаков X и вектор целевой переменной y). 
# Возвращает индекс признака и значение порога с наилучшим разбиением.

def best_split(X: np.ndarray, y: np.ndarray) -> tuple[int, float]:
    """Find the best split for a node"""
    best_feature, best_threshold, entropy_best = None, None, None
    for feature in range(X.shape[1]):
        feat_threshold_best, feat_entropy_best = split(X, y, feature)
        if entropy_best is None or feat_entropy_best < entropy_best:
            best_feature, best_threshold, entropy_best = feature, feat_threshold_best, feat_entropy_best
    return best_feature, best_threshold

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(X.shape)

