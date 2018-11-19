from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

train_data_origin = pd.read_csv('train.csv',header=None)
test_data_origin = pd.read_csv('test.csv',header=None)
x = train_data_origin.iloc[:,:-1]
# print (np.unique(train_data.iloc[:,4]))
le = preprocessing.LabelEncoder()
y = le.fit_transform(train_data_origin.iloc[:,-1].values)

train_data = x.copy()
for col in train_data.columns:
    # if col in cat_column:
        label = preprocessing.LabelEncoder()
        label2 = preprocessing.LabelEncoder()
        label.fit(train_data[col].values)
        label2.fit(test_data_origin[col].values)
        train_data[col] = label.transform(train_data[col].values)
        test_data_origin[col] = label2.transform(test_data_origin[col].values)

rdForest = RandomForestClassifier(criterion='entropy',n_estimators=100)
rdForest.fit(train_data,y)
y_pred = rdForest.predict(test_data_origin)

ans = pd.read_csv('sub.csv')
ans['ans'] = y_pred.flatten().astype(int)
ans.to_csv('answer.csv',index=False)
# X_train, X_test = train_test_split(x,test_size=0.5,random_state=0)
# sc = StandardScaler()
# sc.fit(X_train)
# x_std = sc.transform(x)