import pandas as pd
import statsmodels.api as sm
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\cars24-car-price-cleaned.csv')

df['make'] = df.groupby('make')['selling_price'].transform('mean')
df['model'] = df.groupby('model')['selling_price'].transform('mean')
print(df.head())


from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.model_selection import train_test_split # Sklearn package's randomized data splitting function
df_train, df_test = train_test_split(df, test_size=0.3, random_state=1)

from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler2 = StandardScaler()

scaler = MinMaxScaler()

scaler.fit_transform(df_train)

df_train = pd.DataFrame(scaler.fit_transform(df_train), columns=df.columns)

df_test = pd.DataFrame(scaler.transform(df_test), columns=df.columns)


y_train = df_train['selling_price']
X_train = df_train.drop('selling_price', axis=1)
print(X_train)

y_test = df_test['selling_price']
X_test = df_test.drop('selling_price', axis=1)


print(X_train)


# Now comes the statsmodel part

## 1 Add a constant

X_sm = sm.add_constant(X_train)  # Statmodels default is without intercept, to add intercept we need to add constant.
print(X_sm)

# Fit a Linear Regression - It is called OLS
model = sm.OLS(y_train, X_sm)
results = model.fit()
print(results.summary())

# Let's look at few of the variables in this table:

# Dep. Variable: This column displays the name of the dependent variable being predicted in the regression.

# Model: It provides a concise representation of the model type and method used, such as "OLS" (Ordinary Least Squares).

# R-squared: Represents the coefficient of determination (R-squared) value.

# Adj. R-squared: This is the adjusted R-squared value, which accounts for the number of predictors in the model and adjusts the R-squared accordingly.

# Coefficients Table:

# coef: Estimated coefficients for each predictor.
# std err: Standard error of the coefficients.
# t: t-statistic for testing the hypothesis that the coefficient is different from zero.
# P>|t|: p-value corresponding to the t-statistic.
# [0.025 0.975]: 95% confidence interval for the coefficients.




# VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Statmodels implementation of Linear regression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = df[df.columns.drop('selling_price')]
y = df["selling_price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

scaler = StandardScaler()
X_tr_scaled = scaler.fit_transform(X_train)

X_sm = sm.add_constant(X_tr_scaled)  #Statmodels default is without intercept, to add intercept we need to add constant

sm_model = sm.OLS(y_train, X_sm).fit()

print(sm_model.summary())

vif = pd.DataFrame()

X_t = pd.DataFrame(X_tr_scaled, columns=X_train.columns)
print(X_t)

vif['Features'] = X_t.columns
print(vif)

print(X_t.values)


vif['VIF'] = [variance_inflation_factor(X_t.values, i) for i in range(X_t.shape[1])]
vif = vif.sort_values(by = "VIF", ascending = False)
vif['VIF'] = round(vif['VIF'], 2)
print(vif)