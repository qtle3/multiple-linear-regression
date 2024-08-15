import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

_
df = pd.read_csv("50_Startups.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
