import pandas as pd
from sklearn import tree

dataset = pd.read_csv("DataSet.csv")

X = dataset.iloc[:, 1:]
y = dataset.iloc[:, 0]

model = tree.DecisionTreeClassifier()
model = model.fit(X, y)

print(model.predict([[172, 89, 41.5]]))
