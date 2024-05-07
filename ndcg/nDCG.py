from typing import List

import numpy as np


def normalized_dcg(relevance: List[float], k: int, method: str = "standard") -> float:
    """Normalized Discounted Cumulative Gain.

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
    if k == 0:
        return 0
    # if k > len(relevance) or k < 0 or len(relevance == 0): 
    #     raise ValueError

    relevance_k = relevance[:k]
    sorted_relevance_k = np.sort(relevance)[::-1][:k]

    def count_dcg(relevance: List[float]):
        '''Counts the value of discounted cumulative gain for whole list using standard method'''
        log_k = np.log2(np.arange(2, len(relevance) + 2))
        return np.sum(relevance / log_k)
    
    def count_ind_dcg(relevance: List[float]):
        '''Counts the value of discounted cumulative gain for whole list using industry method'''
        log_k = np.log2(np.arange(2, len(relevance) + 2))
        return np.sum((np.power(2, relevance) - 1) / log_k)
    
    if method == 'standard':
        score = count_dcg(relevance_k) / count_dcg(sorted_relevance_k)
    elif method == 'industry':
        score = count_ind_dcg(relevance_k) / count_ind_dcg(sorted_relevance_k)
    else:
        raise ValueError
    return score
