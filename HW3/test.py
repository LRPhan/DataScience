import pandas as pd
from sklearn import preprocessing

header_name = ['Age', 'Workclass','fnlwgt', 'Education', 'Education-num', 'Marital-status', 'Occupation', 'Relationship', 'Race', 'Sex', 'Capital-gain', 'Capital-loss', 'Hours-per-week', 'Native-country']
train_header = header_name + ['target']
cat_column = ['Workclass', 'Education', 
        'Marital-status', 'Sex', 'Occupation', 'Education-num',
        'Relationship', 'Race', 'Native-country']


def preprocess(training, testing):
    y_train = training['target'].values
    training = training.drop(['target'], axis=1)

    for col in training.columns:
        if col in cat_column:
            label = preprocessing.LabelEncoder()
            label.fit(training[col].values)
            training[col] = label.transform(training[col].values)
            testing[col] = label.transform(testing[col].values)
    if 'target' in testing.columns:
        y_test = testing['target'].values
        testing = testing.drop(['target'], axis=1)
        return training, y_train, testing, y_test
    return training, y_train, testing
train_data = pd.read_csv('train.csv',header=None,names=train_header)
