# Новые пары
# Вас попросили написать маленькую, но важную функцию, которая дополняет матчи, найденные моделью.
# Если товары 1 и 2 – матчи, а также товары 7 и 2 – матчи, то логично сделать вывод, что 1 и 7 тоже матч.
# В данном случае мы не разделяем товары на наши и и товары конкурентов
# Напишите функцию, которая выполняет описанный постпроцессинг предсказаний:
# На входе и выходе ожидается список из tuple. Список на выходе должен быть отсортирован, не содержать дублей и в каждой паре на первом месте товар с меньшим индексом.

from typing import List, Tuple
from itertools import combinations

def list_check(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Checks pairs of items for matches and generates a list of unique item pairs.

    Args:
        pairs: List of tuples representing pairs of items.

    Returns:
        List of unique item pairs that satisfy the conditions of the task.
    """
    matches = set(pairs[0])
    for pair in pairs:
        pair_set = set(pair)                                                                   
        if pair_set & matches and not matches >= pair_set:                              # Check if the pair has common elements with matches and is not a subset of matches
            matches.update(pair_set)
    return [tuple(x) for x in combinations(matches, 2)] 

def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Extends the list of item pairs considering the transitivity of matches.

    Args:
        pairs: List of tuples representing pairs of items.

    Returns:
        Extended list of unique item pairs that satisfy the conditions of the task.
    """
    if not pairs:
        return []
    pairs_copy = [tuple(sorted(pair)) for pair in pairs]                                # Sort and convert pairs to tuples
    matches = []
    
    while pairs_copy:
        extended_pairs = list_check(pairs_copy)
        matches += extended_pairs
        pairs_copy = list(set(pairs_copy).difference(set(extended_pairs)))              # Remove the processed pairs
    return sorted(matches)

# assert extend_matches([(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9)]) == [(1, 2), (1, 3), (1, 5), (2, 3), (2, 5), (3, 5), (4, 6), (4, 7), (6, 7), (8, 9)]
# assert extend_matches([(1, 2)]) == [(1, 2)]
# %timeit extend_matches([(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9)])
