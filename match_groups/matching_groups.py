# Отлично, работает как часы. Однако мы с командой посидели-подумали и пришли к выводу, что работать с парами не так удобно, как с группами матчей.
# Если товары (1, 2) и (7, 2) – матчи, почему бы не объединить их в одну группу (1, 2, 7)? Такой формат записи более удобен.
# Более того, из одних "источников правды" приходят данные в одном формате (группами), из других в формате пар (из модели).
# Формат match-групп кажется более универсальной записью.
# Давайте обновим наш постпроцессинг, чтобы он работал как с парами, так и с тройками товаров, четвёрками и другими наборами товаров.
# Формат данных на входе и выходе аналогичный – список из tuple.
# Требования аналогичные, необходимо вернуть группы матчей, без дубликатов. 
# Везде сортировка по возрастанию (как списка, так и товаров внутри групп).
from typing import List, Tuple

def list_check(groups: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Check the list of groups for common elements and return the extended group.

    Args:
        groups (List[Tuple[int, int]]): List of groups to check.

    Returns:
        List[Tuple[int, int]]: Extended group with common elements.
    """
    matches = set(groups[0])                                                # Initialize the matches with the first group
    for group in groups:
        group_set = set(group)
        if group_set & matches and not matches >= group_set:                # Check if the group has common elements with matches and is not a subset of matches
            matches.update(group_set)
    return matches

def extend_matches(groups: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Extend the matches based on the list of groups.

    Args:
        groups (List[Tuple[int, int]]): List of groups to extend matches.

    Returns:
        List[Tuple[int, int]]: Extended matches.
    """
    groups_copy = sorted(groups)                                             # Sort the groups for consistency
    matches = []

    while groups_copy:
        extended_groups = list_check(groups_copy)                            # Find the extended group of common elements   
        matches.append(tuple(sorted(extended_groups)))
        new_groups_copy = []
        for group in groups_copy:                                            # Filter out groups that are subsets of the extended group
            if not extended_groups >= set(group):
                new_groups_copy.append(group)
        groups_copy = new_groups_copy
    return matches

