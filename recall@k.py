from typing import List
import numpy as np

def recall_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """
    Calculate recall at top-k.

    Args:
        labels (List[int]): True labels.
        scores (List[float]): Predicted scores.
        k (int): Top-k value.

    Returns:
        float: Recall at top-k.
    """
    if k > len(labels):
        k = len(labels)
    if k == 0 or not labels:
        return 0
    k_indices = np.argsort(scores)[::-1][:k]
    k_labels_sorted = [labels[i] for i in k_indices]

    tp = np.sum(k_labels_sorted)
    tpfn = np.sum(labels)
    if tpfn == 0:
        return 0.0
    return tp / tpfn

def precision_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """
    Calculate precision at top-k.

    Args:
        labels (List[int]): True labels.
        scores (List[float]): Predicted scores.
        k (int): Top-k value.

    Returns:
        float: Precision at top-k.
    """
    if k > len(labels):
        k = len(labels)
    if k == 0 or not labels:
        return 0
    k_indices = np.argsort(scores)[::-1][:k]
    k_labels_sorted = [labels[i] for i in k_indices]

    tp = np.sum(k_labels_sorted)
    return tp / k

def specificity_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """
    Calculate specificity at top-k.

    Args:
        labels (List[int]): True labels.
        scores (List[float]): Predicted scores.
        k (int): Top-k value.

    Returns:
        float: Specificity at top-k.
    """
    if k > len(labels):
        k = len(labels)
    if k == 0 or not labels:
        return 0
    indices = np.argsort(scores)[::-1]
    labels_sorted = [labels[i] for i in indices]

    tn = len(labels_sorted[k:]) - np.sum(labels_sorted[k:])
    fp = k - np.sum(labels_sorted[:k])
    if tn + fp == 0:
        return 0.0
    return tn / (tn + fp)

def f1_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """
    Calculate F1 score at top-k.

    Args:
        labels (List[int]): True labels.
        scores (List[float]): Predicted scores.
        k (int): Top-k value.

    Returns:
        float: F1 score at top-k.
    """
    p = precision_at_k(labels, scores, k)
    r = recall_at_k(labels, scores, k)
    if np.isclose(p + r, 0):
        return 0.0
    return 2 * p * r / (p + r)
