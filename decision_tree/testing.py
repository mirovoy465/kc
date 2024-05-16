import numpy as np
import pandas as pd 
from decision_tree_class import DecisionTreeRegressor       
data = pd.read_csv("D:/kc/decision_tree/data.csv")
y = np.array(data["delay_days"])
X = data.drop("delay_days", axis=1).values
tree = DecisionTreeRegressor(10)
tree.fit(X, y)

print(tree.predict(X[0:10]), y[0:10])