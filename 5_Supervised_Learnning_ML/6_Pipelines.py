# Necessary imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sklearn imports
# from sklearn import linear_model
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Ridge
# from sklearn.linear_model import Lasso
# from sklearn.model_selection import GridSearchCV

import os

# hide warnings
# import warnings
# warnings.filterwarnings('ignore')


# reading the dataset
cars = pd.read_csv("C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\CarPrice_Assignment.csv")
print(cars.sample(4))
print()
print(cars.dtypes)

print(cars['symboling'].astype('category').value_counts())


print(cars['aspiration'].astype('category').value_counts())