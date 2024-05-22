from typing import List, Tuple
from functools import reduce

# Из списка продаж фильтровать те, что превышают определенную сумму, и применить к ним налог.
def sales_with_tax(sales: List[float], tax_rate: float, threshold: float = 300) -> List[float]:
    """
    Filters sales that exceed a certain amount and applies tax to them.

    Args:
        sales (List[float]): List of sales.
        tax_rate (float): Tax rate.
        threshold (float): Threshold sales amount (default is 300).

    Returns:
        List[float]: List of sales with applied tax.
    """
    filtered_sales = filter(lambda x: x > threshold, sales)
    taxed_sales = map(lambda x: round(x * (1 + tax_rate)), filtered_sales)
    return list(taxed_sales)

sales = [100, 200, 300, 400, 500]
threshold = 250
tax = 0.1
assert sales_with_tax(sales, tax, threshold) == [330., 440., 550.]

# Суммировать продажи после фильтрации по минимальной сумме продажи.
def sum_sales(sales: List[float], threshold: float = 300) -> float:
    """
    Sums up sales after filtering by minimum sales amount.

    Args:
        sales (List[float]): List of sales.
        threshold (float): Threshold sales amount (default is 300).

    Returns:
        float: Total sales amount.
    """
    filtered_sales = filter(lambda x: x > threshold, sales)
    sum_threshold_sales = float(reduce(lambda x, y: x + y, filtered_sales))
    return sum_threshold_sales

sales = [150, 250, 350, 450, 550]
threshold = 250
assert sum_sales(sales, threshold) == 1350

# Найти средний возраст клиентов, чей возраст превышает определенный порог.
def average_age(ages: List[int], threshold: int = 30) -> float:
    """
    Finds the average age of clients whose age exceeds a certain threshold.

    Args:
        ages (List[int]): List of client ages.
        threshold (int): Threshold age (default is 30).

    Returns:
        float: Average age of clients.
    """
    threshold_ages = list(filter(lambda x: x > threshold, ages))
    if not threshold_ages:
        return 0
    sum_threshold_ages = reduce(lambda x, y: x + y, threshold_ages)
    return sum_threshold_ages/len(threshold_ages)

ages = [22, 35, 42, 55, 67, 18, 29]
threshold = 25
assert average_age(ages, threshold) == 45.6

# Увеличить цену каждого товара на 20% и отфильтровать те, чья итоговая цена превышает определенный порог.
def increased_prices(prices: List[float], increase_rate: int = 0.2, threshold: float = 300) -> List[float]:
    """
    Increases the price of each item by 20% and filters those whose final price exceeds a certain threshold.

    Args:
        prices (List[float]): List of item prices.
        increase_rate (int): Percentage increase in price (default is 0.2).
        threshold (float): Threshold price (default is 300).

    Returns:
        List[float]: List of prices after increase and filtering.
    """
    increased_prices_map = map(lambda x: x * (1 + increase_rate), prices)
    filtered_prices = list(filter(lambda x: x > threshold, increased_prices_map))
    return filtered_prices

prices = [20, 30, 40, 50, 60]
increase_rate = 0.2
threshold = 40
assert increased_prices(prices, increase_rate, threshold) == [48., 60., 72.]

# Рассчитайте средневзвешенную цену проданных товаров. Взвешивать нужно на количество продаж. 
# Т.е. количество выступает как вес в формуле средневзвешенного.
def weighted_sale_price(sales: List[Tuple[int, int]]) -> float:
    """
    Calculates the weighted average price of sold items based on the quantity of sales.

    Args:
        sales (List[Tuple[int, int]]): List of tuples where the first element is the item price and the second is the quantity sold.

    Returns:
        float: Weighted average price of sold items.
    """
    total_weighted_price = reduce(lambda acc, x: acc + x[0] * x[1], sales, 0)
    total_quantity = reduce(lambda acc, x: acc + x[1], sales, 0)
    return total_weighted_price / total_quantity

sales = [(120, 2), (300, 5), (150, 3), (400, 1), (250, 4)]
assert weighted_sale_price(sales) == 239.33333333333334


