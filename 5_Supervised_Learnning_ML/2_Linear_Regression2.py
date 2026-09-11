import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Displaying our data
import pandas as pd
import numpy as np
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\train-cars24-car-price.csv')
data.head()

# using single feature to predict selling price of a car
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.title('MaxPower vs. Price')
sns.scatterplot(data=data, x='max_power', y='selling_price');


def estimate_charges(maxpower, w, b):
    return w * maxpower + b


w = 50
b = 100

maxpower = data.max_power  # From data

estimated_charges = estimate_charges(maxpower, w, b)
print(estimated_charges) #predicted value


print(plt.figure(figsize=(10,6)))

print(plt.plot(maxpower, estimated_charges, 'y-o'));

print(plt.xlabel('MaxPower'));
print(plt.ylabel('Estimated Price'));
print(plt.show())