# Напишите функцию-генератор username_generator, которая принимает количество записей n и опционально списки имен и фамилий.
# Если списки не заданы, используются значения по умолчанию. Для этого внутри генератора определите самостоятельно два списка, 
# состоящие из нескольких значений: список имен и список фамилий.
# Функция создает словарь для каждого пользователя, содержащий поля id, first_name и last_name. 
# ID пользователя должен быть уникальным и соответствовать порядковому номеру генерации. 
# Имена и фамилии выбираются случайным образом из предоставленных или стандартных списков.

import random
def username_generator(n, first_names=None, last_names=None):
    """
    Generate user dictionaries with random first names and last names.

    Args:
        n (int): Number of user dictionaries to generate.
        first_names (list, optional): List of first names to choose from. Defaults to ['Alice', 'Bob', 'Charlie', 'David'].
        last_names (list, optional): List of last names to choose from. Defaults to ['Smith', 'Johnson', 'Williams', 'Jones'].

    Yields:
        dict: User dictionary with keys 'id', 'first_name', and 'last_name'.
    """
    if first_names is None:
        first_names = ['Alice', 'Bob', 'Charlie', 'David']
    if last_names is None:
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones']
    for i in range(n):
        user = {'id' : i+1,
                'first_name' : random.choice(first_names),
                'last_name' : random.choice(last_names)}
        yield user

# Напишите функцию-генератор data_generator, которая генерирует пары (x, y), где x - это последовательно возрастающие целые числа, 
# начиная с 0, а y - случайное число в заданном диапазоне от 0 до 100. 
# Генератор должен принимать один параметр - количество генерируемых пар n.

def data_generator(n):
    """
    Generate pairs (x, y) where x is sequentially increasing integers starting from 0, and y is a random number in the range from 0 to 100.

    Args:
        n (int): Number of pairs to generate.

    Yields:
        tuple: Pair of (x, y) where x is an integer and y is a random number.
    """
    for i in range(n):
        y = random.randint(0, 100)
        yield i, y

