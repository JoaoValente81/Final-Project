import pandas as pd
import numpy as np

import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('extreme2')

X=df.drop(columns=['extreme', 'year', 'month', 'day', 'DataHoraAlerta', 'Date', 'tmin', 'AreaTotal_ha', 'Codigo_ANEPC', 'Unnamed: 0'])
y=df['extreme']

X_train, X_test, y_train, y_test=train_test_split(X,y, random_state=1, test_size=0.2)

lr=LogisticRegression()

## train the model
lr.fit(X_train, y_train)

print(lr.predict(X_test))

print(lr.score(X_test, y_test))

## Save the model
pkl_file='lr_model.pkl'

with open(pkl_file, 'wb') as file:
    pickle.dump(lr, file)