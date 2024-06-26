# Мы B2B финтех стартап — предоставляем депозиты/кредиты, куплю/продажу ценных бумаг и другие финансовые инструменты. 
# У нас небольшое число очень крупных клиентов. Мы заключаем контракты минимум на 1 год. 
# Для принятия решения о сотрудничестве мы разрабатываем модель, которая для потенциального клиента прогнозирует LTV 
# (LifeTime Value, сколько денег нам принесёт клиент за всё время, что будет пользоваться нашим сервисом).
# Подумайте, что предпочтительнее: недооценить или переоценить стоимость потенциального клиента?

# Вам необходимо выбрать или разработать функцию, отражающую ошибку для оценки модели прогноза LTV.

import numpy as np

def ltv_error(y_true: np.array, y_pred: np.array) -> float:
    error = np.sqrt((np.log1p(y_pred)-np.log1p(y_true))**2)
    error = np.mean(np.where(y_pred > y_true, 3 * error, error))
    return error
