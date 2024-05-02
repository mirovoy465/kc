# Вы решаете задачу прогнозирования спроса в быстро развивающемся стартапе KarpovExpress, где количество новых товаров увеличивается на десятки штук каждый месяц.
# Прогноз продаж надо делать каждую неделю в рублях или товарах, а на товары-новинки нет данных и истории продаж. 
# Модель прогнозирования спроса не выдает ничего адекватного и не умеет работать с NaN пропусками. 
# Но есть идея — пропуски для товаров-новинок можно заполнить среднем значением продаж по категориям этого товара!
# Прогнозирование для новых товаров - очень важная вещь, 
# которая поможет новым пользователям чаще видеть релевантные товары в рекомендациях или бизнесу предсказывать поведения пользователей.
# Вы решили дописать функцию fillna_with_mean, которая заполняет пропуски в колонке target ее средними значениями по группам. Группировка происходит по колонке group. 

import pandas as pd
import numpy as np


def fillna_with_mean(df: pd.DataFrame, target: str, group: str) -> pd.DataFrame:
    '''Fills the NA values with mean values within given target category'''

    if not df[target].isna().any():
        return df
    
    df_copy = df.copy()
    mean_values = np.floor(df_copy.groupby(group)[target].transform('mean'))
    df_copy.loc[df_copy[target].isnull(), target] = mean_values
    return df_copy
    
# data = pd.DataFrame({
#     'group': ['A', 'A', 'B', 'B', 'A', 'B', 'B'],
#     'target': [1, 2, np.nan, 4, 5, 5.2, np.nan]
# })


# print(fillna_with_mean(data, 'target', 'group'))