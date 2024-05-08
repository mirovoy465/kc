# Ваш коллега написал код для подсчета нескольких бизнес метрик:

# Общая прибыль
# Маржинальность (отношение прибыли к выручке)
# Средняя наценка (отношение прибыли к затратам)
# Помогите ему написать для них юнит-тесты, используя Pytest.

import metrics


def test_profit() -> None:
    """Test the profit function.

    Returns
    -------
    None
    """
    assert metrics.profit([1, 2, 3], [1, 1, 1]) == 3


def test_margin() -> None:
    """Test the margin function.

    Returns
    -------
    None
    """
    assert metrics.margin([1, 2, 3], [1, 1, 1]) == 0.5


def test_markup() -> None:
    """Test the markup function.

    Returns
    -------
    None
    """
    assert metrics.markup([1, 2, 3], [1, 1, 1]) == 1
