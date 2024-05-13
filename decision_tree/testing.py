from decision_tree_class import DecisionTreeRegressor
import pandas as pd

data = pd.read_csv('data.csv')
y = data['delay_days']
X = data.drop('delay_days', axis=1)
tree = DecisionTreeRegressor(5)
tree.fit(X, y)
