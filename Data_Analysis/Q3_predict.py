import numpy as np
import pandas as pd
import pydotplus
import csv

import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"heart_data.csv")
print([column for column in df])
print(df.shape)

def encoder(data):
#Map the categorical variables to numbers to work with scikit learn
    for col in data.columns:
        if data.dtypes[col] == "object":
            le = LabelEncoder()
            le.fit(data[col])
            data[col] = le.transform(data[col])
    return data

df = df.dropna(axis=1)
print([column for column in df], df.shape)
data = encoder(df)
data = data.values * 1

print(data)

X = data[:,1:]
Y = data[:,0]
print(X.shape)
print(Y.shape)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

cross_validation_scores= []
cross_validation_mean = []
cross_validation_std = []

for k in range(1,15):
    model = DecisionTreeClassifier(max_depth=k)
    scores = cross_val_score(model,x_train,y_train)
    cross_validation_scores.append(scores.tolist())
    cross_validation_mean.append(scores.mean())
    cross_validation_std.append(scores.std())
    print(k,scores.mean())

plt.rcParams['figure.figsize'] = (16.0, 7.0)
plt.style.use('seaborn-darkgrid')
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for i in range(len(list)):
  plt.scatter([list[i]] * 5, cross_validation_scores[i])

plt.errorbar(list, cross_validation_mean, yerr=cross_validation_std,ecolor='royalblue')
plt.title('5-Fold Cross-validation')
plt.xlabel('max_length in DecisionTree')
plt.ylabel('Cross-validation accuracy')
plt.show()

model = DecisionTreeClassifier(max_depth=6)
model.fit(x_train, y_train)
y_pre = model.predict(x_test)
acc_score = accuracy_score(y_test, y_pre)
print(acc_score)

dot_data = tree.export_graphviz(model, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("heartdisease_2.pdf")

