# Ваша задача: написать функцию, которая проверяет, есть ли значимое различие средних ошибок прогнозов времени доставки
# в контрольной и экспериментальных выборках (в группах A и B). 

from scipy.stats import ttest_ind
from typing import List, Tuple

def ttest(
    control: List[float],
    experiment: List[float],
    alpha: float = 0.05,
) -> Tuple[float, bool]:
    """
    Perform a two-sample t-test for the means of two independent samples.

    Parameters:
    control : List[float]
        List of values for the control group.
    experiment : List[float]
        List of values for the experimental group.
    alpha : float, optional
        Significance level for the test (default is 0.05).

    Returns:
    Tuple[float, bool]
        p-value of the t-test and a boolean indicating if the null hypothesis is rejected.
    """
    _, p_value = ttest_ind(control, experiment)
    result = bool(p_value < alpha)
    return p_value, result
