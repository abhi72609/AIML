import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np


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
print(plt.ylabel("Consumption"))
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

X = pd.DataFrame({
    "Age": [20, 30, 40],
    "Height": [160, 170, 180]
})

print(X)
poly = PolynomialFeatures(degree=2, include_bias=False)

x_poly = poly.fit_transform(X)
print(x_poly)
print(poly.get_feature_names_out(X.columns))








# Store R² scores for each polynomial degree
r2_train = []
r2_test = []

# Polynomial degrees we want to compare
degrees = [1, 2, 3, 10]


# Create one figure with 3 subplots
fig, axes = plt.subplots(1, 4, figsize=(18, 5), sharey=True)


# Loop through each polynomial degree
for ax, degree in zip(axes, degrees):

    # Create and fit the Polynomial Regression model
    pipeline = Pipeline([
        ('poly_features', PolynomialFeatures(degree=degree)),
        ('model', LinearRegression())
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Predictions
    y_pred_train = pipeline.predict(X_train)
    y_pred_test = pipeline.predict(X_test)

    # Store R² scores
    r2_train.append(
        metrics.r2_score(y_train, y_pred_train)
    )

    r2_test.append(
        metrics.r2_score(y_test, y_pred_test)
    )

    # Sort data for smooth curves
    train_order = np.argsort(X_train.flatten())
    test_order = np.argsort(X_test.flatten())

    # Plot training data
    ax.scatter(
        X_train,
        y_train,
        color="blue",
        label="Train Data"
    )

    # Plot training prediction
    ax.plot(
        X_train[train_order],
        y_pred_train[train_order],
        color="blue",
        linewidth=2,
        label="Train Fit"
    )

    # Plot test data
    ax.scatter(
        X_test,
        y_test,
        color="red",
        label="Test Data"
    )

    # Plot test prediction
    ax.plot(
        X_test[test_order],
        y_pred_test[test_order],
        color="red",
        linewidth=2,
        label="Test Prediction"
    )

    # Graph settings
    ax.set_title(f"Degree = {degree}")
    ax.set_xlabel("Year")
    ax.grid(True)
    ax.legend()


# Y-axis label
axes[0].set_ylabel("Power Consumption")

# Adjust spacing
plt.tight_layout()

# Display graphs
plt.show()


# Print R² scores
for degree, train_score, test_score in zip(
    degrees, r2_train, r2_test
):
    print(
        f"Degree {degree}: "
        f"Train R² = {train_score:.3f}, "
        f"Test R² = {test_score:.3f}"
    )




#   BIAS - VARIANCE

