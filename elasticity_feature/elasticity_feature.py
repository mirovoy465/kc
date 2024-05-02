import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# full_data = pd.read_csv('elasticity_query_results.csv', dtype={'sku': int, 'qty' : int, 'price' : float, 'dates': str})

def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:
    '''Return the dataframe with elasticity coefficients for each SKU'''
    
    def calculate_elasticity(price: pd.Series, qty: pd.Series) -> float:
        '''Return the R2 score (measure of elasticity) for a given price and quantity'''

        price = price.values.reshape(-1, 1)
        qty = np.log1p(qty)
        model_fit = LinearRegression().fit(price, qty)
        return r2_score(qty, model_fit.predict(price))
    
    elasticity_df = df.groupby('sku').apply(
        lambda x: calculate_elasticity(x['price'], x['qty'])).reset_index(name='elasticity')

    return elasticity_df

# print(elasticity_df(full_data))