# Наша модель динамического ценообразования на маркетплейсе KarpovExpress предсказывает оборот на завтра в рублях. 
# Прогноз выполняется на основе некоторого набора фичей и цены. Также мы знаем, сколько товаров хранится на складе и доступно для продажи. 
# Предполагается, что на данные товары нет никаких дополнительных промоакций, скидок и для каждого покупателя цена одинакова.

# Колонки таблицы
# sku – SKU (Stock Keeping Unit), уникальный ID товара (тип int)
# gmv – GMV (Gross Merchandise Volume), аналог розничного товарооборота (тип float)
# stock – число единиц товара на складе (тип int)
# price – цена на товар (тип float)
# Формула расчёта: GMV = (цена) * (штук продано)

# Задача
# Необходимо написать функцию для постобработки предсказаний модели.

import pandas as pd

def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:
    '''Limit GMV accounting for available stock and previous GMV values'''

    df_copy = df.copy()
    max_stock = (df['gmv'] / df['price']).clip(upper = df['stock']).astype(int)
    df_copy['gmv'] = max_stock * df['price']
    return df_copy

# data = {
#     'sku': [100, 200, 300],
#     'gmv': [400, 350, 500],
#     'price': [100, 70, 120],
#     'stock': [3, 10, 5]
# }

# # Создаем DataFrame
# df = pd.DataFrame(data)
# print(df)
# print(limit_gmv(df))
