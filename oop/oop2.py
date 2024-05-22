# Есть базовый класс RandomSampler, реализующий случайное семплирование данных из датафрейма.
# Вам необходимо создать дочерний класс UniqueRandomСolumnSampler, который наследуется от RandomSampler и переопределяет его функциональность.
# Дочерний класс должен иметь возможность выбора уникальных значений из указанного столбца.
# Ожидаемое поведение:
# RandomSampler уже реализован и использует встроенный метод sample для случайного семплирования данных из датафрейма
# UniqueColumnSampler должен выбирать уникальные значения из указанного столбца и возвращать новый датафрейм с этими значениями.
# Результирующий датафрейм содержит только одну колонку.

import random
import pandas as pd

class RandomSampler:
    """Randomly samples data from a dataframe."""

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def get_num_rows(self):
        """Returns the number of rows in the dataframe."""
        return len(self.dataframe)

    def sample_data(self, num_samples: int):
        """Samples a specified number of rows from the dataframe."""
        return self.dataframe.sample(num_samples)


class UniqueColumnSampler(RandomSampler):
    """Samples unique values from a specified column in the dataframe."""

    def __init__(self, dataframe: pd.DataFrame, column_name: str):
        super().__init__(dataframe)
        self.column_name = column_name

    def sample_data(self, num_samples: int):
        """Samples unique values from the specified column."""
        unique_values = list(self.dataframe[self.column_name].unique())
        sampled_values = random.sample(unique_values, min(num_samples, len(unique_values)))
        return pd.DataFrame({self.column_name: sampled_values})


data = {
    'A': [random.choice(['apple', 'banana', 'cherry']) for _ in range(100)],
    'B': [random.randint(1, 10) for _ in range(100)],
    'C': [random.choice(['red', 'green', 'blue']) for _ in range(100)]
}

df = pd.DataFrame(data)
print(UniqueColumnSampler(df, 'B').sample_data(5))