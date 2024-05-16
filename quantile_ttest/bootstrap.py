# Задача
# Реализуйте bootstrapped t-тест для сравнения квантилей ошибок прогноза.
# Формат выходных данных совпадает с прошлым шагом.

import numpy as np
from typing import List, Tuple
from scipy.stats import ttest_ind

def bootstrapped_quantile(x: List[float], n_bootstraps: int, quantile: float) -> List[float]:
    """Bootstrapped median distribution"""
    bootstrapped_quantiles = []
    
    for _ in range(n_bootstraps):
        bootstrapped_sample = np.random.choice(x, size=len(x), replace=True)
        bootstrapped_quantiles.append(np.percentile(bootstrapped_sample, quantile))
        
    return bootstrapped_quantiles

def quantile_ttest(
    control: List[float],
    experiment: List[float],
    alpha: float = 0.05,
    quantile: float = 0.95,
    n_bootstraps: int = 1000,
) -> Tuple[float, bool]:
    """
    Bootstrapped t-test for quantiles of two samples.
    """
    control_bm = bootstrapped_quantile(control, n_bootstraps, quantile)
    experiment_bm = bootstrapped_quantile(experiment, n_bootstraps, quantile)
    _, p_value = ttest_ind(control_bm, experiment_bm)
    result = bool(p_value < alpha)
    return p_value, result
