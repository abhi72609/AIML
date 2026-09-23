import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics

# fetching data
elec_cons = pd.read_csv(
    "C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\total-electricity-consumption-us.csv",
    sep=',',
    header=0
)

print(elec_cons.head())

# total number of observations
elec_cons.shape


plt.scatter(
    x=elec_cons['Year'],
    y=elec_cons['Consumption']
)

print(plt.xlabel("Year"))
print(plt.ylabel("Selling Price"))
print(plt.show())


size = len(elec_cons.index)
index = range(0, size, 5)

train = elec_cons[~elec_cons.index.isin(index)]
test = elec_cons[elec_cons.index.isin(index)]

print(len(train))
print(len(test))


X_train = train.Year.values.reshape(-1, 1)  # Making X two dimensional
y_train = train.Consumption
print(y_train)
X_test = test.Year.values.reshape(-1, 1)    # Making X two dimensional
y_test = test.Consumption
print(y_test)


from sklearn.preprocessing import PolynomialFeatures

PolynomialFeatures(degree=2)

X = pd.DataFrame({
    "Age": [20, 30, 40],
    "Height": [160, 170, 180]
})

PolynomialFeatures(degree=2)