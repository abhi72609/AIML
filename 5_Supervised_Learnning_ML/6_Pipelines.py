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

# drivewheel: frontwheel, rarewheel or four-wheel drive
print(cars['drivewheel'].astype('category').value_counts())


sns.distplot(cars['wheelbase'])
print(plt.show())

sns.distplot(cars['price'])
print(plt.show())



# Data Exploration
# to perform linear regression the target variable should be linearly related.


# Select all the numerical type columns
cars_numeric = cars.select_dtypes(include=['float64', 'int64'])
print(cars_numeric.head())

cars_numeric = cars_numeric.drop(['symboling'], axis=1)


# plt.figure(figsize=(20, 10))
# sns.pairplot(cars_numeric)
# print(plt.show());

cor = cars_numeric.corr()
print(cor)


# price_corr = (
#     cars.select_dtypes(include="number")
#         .corr()["price"]
#         .sort_values(key=lambda x: x.abs(), ascending=False)
# )

# print(price_corr)


# prompt = f"""
# We are building a linear regression model for car price.

# These are Pearson correlations with price:

# {price_corr.to_string()}

# Give me only:
# 1. Five useful EDA observations
# 2. Two possible multicollinearity checks
# 3. Two warnings about what correlation does NOT prove

# Do not invent facts outside these numbers.
# """

# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {"role": "user", "content": prompt}
#     ]
# )


# print(dir(response))
# print(response.choices[0].message.content)



#   DATA CLEANING

cars['symboling'] = cars['symboling'].astype('object')
cars.info()


print(cars['CarName'][:10])
# feature Engineering: Extracting car company name from CarName column
cars['car_company'] = cars['CarName'].str.split().str[0]
print(cars['car_company'])

#   Regular Expressions
## Method 2 - regrex
# p = re.compile(r'\w+-?\w+')
# cars['car_company'] = cars['CarName'].apply(lambda x: re.findall(p, x)[0])
# print(cars['car_company'])


print(cars['car_company'].value_counts())

# replacing misspelled car_company names

# volkswagen
cars.loc[(cars['car_company'] == "vw") |
         (cars['car_company'] == "vokswagen")
         , 'car_company'] = 'volkswagen'

# porsche
cars.loc[cars['car_company'] == "porcshce", 'car_company'] = 'porsche'

# toyota
cars.loc[cars['car_company'] == "toyouta", 'car_company'] = 'toyota'

# nissan
cars.loc[cars['car_company'] == "Nissan", 'car_company'] = 'nissan'

# mazda
cars.loc[cars['car_company'] == "maxda", 'car_company'] = 'mazda'

print(cars['car_company'].astype('category').value_counts())

print(cars.describe().T)


# Column Transformer
# Extracting out the numerical columns from the cleaned CARS24 dataset
num_cols = cars.select_dtypes(include='number').columns
print(num_cols)

# Extracting out the categorical columns from the cleaned CARS24 dataset
cat_cols = cars.select_dtypes(include='object').columns
print(cat_cols)

# 1. Columns for Standard Scaling = ['car_ID','carwidth','enginesize','compressionratio','citympg']
# 2. Columns for Min Max Scaling = ['wheelbase','carheight','boreratio','horsepower','highwaympg']
# 3. Columns for Max Absolute Scaling = ['carlength','curbweight','stroke','peakrpm','price']






from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

# defining the transformer
scaling_transformer = ColumnTransformer(transformers =
[
    ('Standard Scaler', StandardScaler(), ['car_ID','carwidth','enginesize','compressionratio','citympg']),
    ('Min-Max Scaler', MinMaxScaler(), ['wheelbase','carheight','boreratio','horsepower','highwaympg']),
    ('Max Absolute Scaling', MaxAbsScaler(), ['carlength','curbweight','stroke','peakrpm','price'])
],
remainder='drop').set_output(transform='pandas')
print(scaling_transformer)

# Need to explain about some selected parameters of column transformer:

# 1. remainder and what does the values passthrough and drop signify here.
# 2. verbose_feature_names_out and what does verbosity exactly mean.
# 3. set_output(transform='pandas') and mention that by default the output of ColumnTransformer is numpy array. This attribute converts the output to pandas DataFrame/Series.
print(cars.columns)



# fitting and transforming the cars dataset as per the created transformer.
scaled_num_cols = scaling_transformer.fit_transform(cars)
print(scaled_num_cols.head())






# Necessary imports for the Encoding part
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

# categories list for the Ordinal encoder part
OE_categories_list = [
    [-2,-1,3,2,1,0],
    ['two','three','four','five','six','eight','twelve']
]




# defining the transformer
encoding_transformer = ColumnTransformer(transformers =
 [
     ('Ordinal encoder', OrdinalEncoder(categories=OE_categories_list), ['symboling','cylindernumber']),
     ('One Hot Encoder', OneHotEncoder(sparse_output=False), ['symboling','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem','car_company'])
 ],
remainder='drop').set_output(transform='pandas')
print(encoding_transformer)

# fitting and transforming the cars dataset as per the created transformer.
encoded_cat_cols = encoding_transformer.fit_transform(cars)
encoded_cat_cols.head()





# Tuning the scaling transformer accordingly for the pipeline
scaling_tf = ColumnTransformer(transformers =
[
    ('Standard Scaler', StandardScaler(), ['car_ID','carwidth','enginesize','compressionratio','citympg']),
    ('Min-Max Scaler', MinMaxScaler(), ['wheelbase','carheight','boreratio','horsepower','highwaympg']),
    ('Max Absolute Scaling', MaxAbsScaler(), ['carlength','curbweight','stroke','peakrpm','price'])
],
remainder='passthrough',verbose_feature_names_out=False).set_output(transform='pandas')

print(scaling_tf)



OE_categories_list = [
    [-2,-1,3,2,1,0],
    ['two','three','four','five','six','eight','twelve']
]

# tuning the encoding transformer for the pipeline
encoding_tf = ColumnTransformer(transformers =
 [
     ('Ordinal encoder', OrdinalEncoder(categories=OE_categories_list), ['symboling','cylindernumber']),
     ('One Hot Encoder', OneHotEncoder(sparse_output=False), ['symboling','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem','car_company'])
 ],
remainder='passthrough', verbose_feature_names_out=False).set_output(transform='pandas')

print(encoding_tf)






# Necessary import for pipeline
from sklearn.pipeline import Pipeline

from sklearn.pipeline import Pipeline

# defining the pipeline
pipeline = Pipeline(steps=
 [
     ('Encoding', encoding_tf),
     ('Scaling', scaling_tf)
 ]).set_output(transform='pandas')

print(pipeline)


preprocessed_data =pipeline.fit_transform(cars)
print(preprocessed_data)





# =========================
# 1. IMPORTS
# =========================

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    MaxAbsScaler,
    OneHotEncoder,
    OrdinalEncoder
)
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


# =========================
# 2. X AND y
# =========================

# price is what we want to predict
X = cars.drop(columns=['price'])
y = cars['price']


# =========================
# 3. TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 4. DEFINE COLUMNS
# =========================

standard_cols = [
    'car_ID',
    'carwidth',
    'enginesize',
    'compressionratio',
    'citympg'
]

minmax_cols = [
    'wheelbase',
    'carheight',
    'boreratio',
    'horsepower',
    'highwaympg'
]

maxabs_cols = [
    'carlength',
    'curbweight',
    'stroke',
    'peakrpm'
]

ordinal_cols = [
    'symboling',
    'cylindernumber'
]

onehot_cols = [
    'fueltype',
    'aspiration',
    'doornumber',
    'carbody',
    'drivewheel',
    'enginelocation',
    'enginetype',
    'fuelsystem',
    'car_company'
]


# =========================
# 5. ORDINAL CATEGORY ORDER
# =========================

ordinal_categories = [
    [-2, -1, 0, 1, 2, 3],
    ['two', 'three', 'four', 'five', 'six', 'eight', 'twelve']
]


# =========================
# 6. ONE PREPROCESSOR
# =========================

preprocessor = ColumnTransformer(
    transformers=[

        ('standard_scaler',
         StandardScaler(),
         standard_cols),

        ('minmax_scaler',
         MinMaxScaler(),
         minmax_cols),

        ('maxabs_scaler',
         MaxAbsScaler(),
         maxabs_cols),

        ('ordinal_encoder',
         OrdinalEncoder(categories=ordinal_categories),
         ordinal_cols),

        ('onehot_encoder',
         OneHotEncoder(handle_unknown='ignore'),
         onehot_cols)
    ],
    remainder='drop'
)


# =========================
# 7. FINAL PIPELINE
# =========================

model = Pipeline(
    steps=[
        ('preprocessing', preprocessor),
        ('linear_regression', LinearRegression())
    ]
)


# =========================
# 8. TRAIN
# =========================

model.fit(X_train, y_train)


# =========================
# 9. PREDICT
# =========================

y_pred = model.predict(X_test)


print()
