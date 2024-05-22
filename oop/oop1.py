# Вашей задачей является создание класса Python для обработки данных DataProcessor.
# Вам следует определить атрибуты, такие как data и processed_data_.
# Напишите метод под названием process, который не принимает параметры.
# Этот метод должен реализовать логику предобработки данных и сохранить результат в атрибут processed_data_.
# Предобработка следующая: Необходимо вычислить отклонение от среднего.
# Напишите метод save_to_file, который принимает имя файла в качестве параметра и сохраняет обработанные данные в указанный файл.
# Каждое значение в списке processed_data_ необходимо сохранять на отдельной строке.
# Если данные не были обработаны, файл сохранять не нужно.
from typing import List, Union

class DataProcessor:
    """A class for processing and saving data."""

    def __init__(self, data: List[Union[int, float]]) -> None:
        """
        Initialize the DataProcessor object with the given data.

        Args:
            data (List[Union[int, float]]): List of integers or floats (default is an empty list).
        """
        self.data = data
        self.processed_data_ = None

    def process(self) -> None:
        """
        Process the data by dividing each element by the mean of the data.
        """
        if len(self.data) == 0:
            return
        mean = sum(self.data) / len(self.data)
        self.processed_data_ = list(map(lambda x: x - mean, self.data))
    
    def save_to_file(self, file_name: str) -> None:
        """
        Save the processed data to a file.

        Args:
            file_name (str): Name of the file to save the data to.
        """
        if self.processed_data_ is None:
            return
        with open(file_name, 'w') as f:
            for item in self.processed_data_:
                f.write(f'{item}\n')

# Example of usage
processor = DataProcessor(data=[1, 2, 3, 4, 5])
processor.process()
processor.save_to_file("processed_data.txt")
