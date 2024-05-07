from typing import List
from DCG import discounted_cumulative_gain
import numpy as np

def avg_ndcg(list_relevances: List[List[float]], k: int, method: str = 'standard') -> float:
    """average nDCG

    Parameters
    ----------
    list_relevances : `List[List[float]]`
        Video relevance matrix for various queries
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

    scores = []
    for relevance in list_relevances:
        sorted_relevance = np.sort(relevance)[::-1]
        scores.append(discounted_cumulative_gain(relevance, k, method) /
                       discounted_cumulative_gain(sorted_relevance, k, method))
    return np.mean(scores)

list_relevances = [
        [0.99, 0.94, 0.88, 0.89, 0.72, 0.65],
        [0.99, 0.92, 0.93, 0.74, 0.61, 0.68], 
        [0.99, 0.96, 0.81, 0.73, 0.76, 0.69]
    ]  
k = 5
method = 'standard'
print(avg_ndcg(list_relevances, k, method))
