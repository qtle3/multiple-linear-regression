# Description: Multiple Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
df = pd.read_csv("50_Startups.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough"
)
X = np.array(ct.fit_transform(X))

# split the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
