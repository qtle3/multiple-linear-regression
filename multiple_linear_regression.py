# Description: Multiple Linear Regression

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# sklearn libraries
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

# Importing the dataset and split the dataset into the independent and dependent variables
df = pd.read_csv("50_Startups.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
print(X)

# Encoding categorical data (State column)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough"
)
X = np.array(ct.fit_transform(X))

# split the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the Multiple Linear Regression model on the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results and compare with the actual results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.column_stack((y_pred, y_test)))
