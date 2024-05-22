# Вы с коллегой разрабатываете пайплайн предобработки данных.
# Вы договорились, что в пайплайне могут использоваться разные методы обработки данных.
# Все эти методы объединяет то, что:
# Они принимают на вход список числовых значений
# Возвращают список числовых значений
# Вы договорились, что каждый метод обработки будет представлять собой отдельный класс.
# Чтобы обеспечить единообразное поведение этих классов, вы договорились что все они будут реализовывать единый интерфейс
# (абстрактный класс) DataPreprocessor, который содержит единственный метод preprocess.
# Метод принимает список чисел и возвращает обработанный список чисел.
# Ваша задача:
# Реализовать абстрактный класс DataPreprocessor с единственным методом preprocess. Метод принимает на вход аргумент data.
# Реализовать 3 дочерних классах OutlierRemover, Normalizer, Encoder. В каждом классе реализуется собственная логика метода preprocess.
from abc import ABC, abstractmethod
from typing import List, Dict, Union


class DataPreprocessor(ABC):
    @abstractmethod
    def preprocess(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """Abstract method to preprocess the input data."""

class OutlierRemover(DataPreprocessor):
    def preprocess(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """Remove outliers from the input data."""
        return [x for x in data if x <= 10]

class Normalizer(DataPreprocessor):
    def preprocess(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """Normalize the input data by dividing each element by 10."""
        return [x / 10 for x in data]

class Encoder(DataPreprocessor):
    def __init__(self, encoding_dict: Dict[str, int]) -> None:
        super().__init__()
        self.encoding_dict = encoding_dict

    def preprocess(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """Encode the input data using the provided encoding dictionary."""
        return [self.encoding_dict.get(str(x), x) for x in data]

# Пример использования OutlierRemover
outlier_remover = OutlierRemover()

data_with_outliers = [1, 2, 3, 100, 5, 6, 7, 8, 9]
cleaned_data = outlier_remover.preprocess(data_with_outliers)

print(f"Исходные данные: {data_with_outliers}")
print(f"Данные без выбросов: {cleaned_data}")

# Пример использования Normalizer
normalizer = Normalizer()

numerical_data = [10, 20, 30, 40, 50]
normalized_data = normalizer.preprocess(numerical_data)

print(f"Исходные числовые данные: {numerical_data}")
print(f"Нормализованные данные: {normalized_data}")
# Пример использования Encoder
encoder = Encoder(encoding_dict={'красный': 1, 'зеленый': 2, 'синий': 3})

categorical_data = ['красный', 'зеленый', 'синий']
encoded_data = encoder.preprocess(categorical_data)

print(f"Исходные категориальные данные: {categorical_data}")
print(f"Закодированные данные: {encoded_data}")
