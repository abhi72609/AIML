import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Displaying our data
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\train-cars24-car-price.csv')
data.head()

# # using single feature to predict selling price of a car
# import seaborn as sns
# import matplotlib.pyplot as plt
# plt.figure(figsize=(10,6))
# plt.title('MaxPower vs. Price')
# sns.scatterplot(data=data, x='max_power', y='selling_price');


# def estimate_charges(maxpower, w, b):
#     return w * maxpower + b


# w = 50
# b = 100

# maxpower = data.max_power  # From data

# estimated_charges = estimate_charges(maxpower, w, b)
# print(estimated_charges) #predicted value and equation of line is y = 50x + 100


# print(plt.figure(figsize=(10,6)))

# print(plt.plot(maxpower, estimated_charges, 'y-o'));

# print(plt.xlabel('MaxPower'));
# print(plt.ylabel('Estimated Price'));
# print(plt.show())



# target = data.selling_price
# print(plt.figure(figsize=(10,6)))
# print(plt.plot(maxpower, estimated_charges, 'y', alpha=0.9));
# print(plt.scatter(maxpower, target, s=8,alpha=0.8));
# print(plt.xlabel('MaxPower'));
# print(plt.ylabel('Price'))
# print(plt.legend(['Estimate', 'Actual']));
# print(plt.show())


# def try_parameters(w, b):
#     maxpower = data.max_power
#     target = data.selling_price

#     estimated_charges = estimate_charges(maxpower, w, b)
#     print(plt.figure(figsize=(10,6)))
#     print(plt.plot(maxpower, estimated_charges, 'r', alpha=0.9));
#     print(plt.scatter(maxpower, target, s=8,alpha=0.8));
#     print(plt.xlabel('MaxPower'));
#     print(plt.ylabel('Price'))
#     print(plt.legend(['Estimate', 'Actual']));
#     print(plt.show())

# try_parameters(0.08, 0.5)

# Input and target
x = data.max_power
y = data.selling_price

# Mean of x and y
x_mean = x.mean()
y_mean = y.mean()

# Calculate weight (w)
w = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()

# Calculate bias (b)
b = y_mean - w * x_mean

print("Best weight:", w)
print("Best bias:", b)

# Predictions
estimated_charges = w * x + b

# Plot actual data
print(plt.figure(figsize=(10, 6)))

print(plt.scatter(x, y, s=8, alpha=0.8))
print(plt.plot(x, estimated_charges, 'r'))

print(plt.xlabel('MaxPower'))
print(plt.ylabel('Selling Price'))
print(plt.legend(['Best Fit Line', 'Actual Data']))
print(plt.show())



df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\train-cars24-car-price.csv')
df.head()

print(len(df))
X = df[["model"]]
y = df["selling_price"]
from sklearn.linear_model import LinearRegression
model = LinearRegression()