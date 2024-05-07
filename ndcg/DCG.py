from typing import List

import numpy as np


def discounted_cumulative_gain(relevance: List[float], k: int, method: str = "standard") -> float:
    """Discounted Cumulative Gain

    Parameters
    ----------
    relevance : `List[float]`
        Video relevance list
    k : `int`
        Count relevance to compute
    method : `str`, optional
        Metric implementation method, takes the values
        `standard` - adds weight to the denominator
        `industry` - adds weights to the numerator and denominator
        `raise ValueError` - for any value

    Returns
    -------
    score : `float`
        Metric score
    """
    if k > len(relevance) or k < 0 or len(relevance) == 0: 
        raise ValueError
    if k == 0:
        return 0

    log_k = np.log2(np.arange(2, k+2))
    relevance_k = relevance[:k]
    if method == 'standard':
        score = np.sum(relevance_k / log_k)
    elif method == 'industry':
        score = np.sum((np.power(2, relevance_k) - 1) / log_k)
    else:
        raise ValueError
    return score
