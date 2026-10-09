

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. Load the Auto MPG dataset
# ---------------------------------------------------------

cData = pd.read_csv(
    "C:\\Users\\hp\\Desktop\\Coding\\AIML\\5_Supervised_Learnning_ML\\auto-mpg.csv"
)

# Check the number of rows and columns in the dataset
print(cData.shape)


# ---------------------------------------------------------
# 2. Remove the 'car name' column
# ---------------------------------------------------------

# 'car name' is not required for our ML model,
# so we remove it.
# axis=1 means we are dropping a column.
cData = cData.drop('car name', axis=1)

print(cData)


# ---------------------------------------------------------
# 3. Convert 'origin' numerical values into categories
# ---------------------------------------------------------

# Original values:
# 1 → American
# 2 → Europe
# 3 → Asia

cData['origin'] = cData['origin'].replace({
    1: 'American',
    2: 'europe',
    3: 'asia'
})


# ---------------------------------------------------------
# 4. One-Hot Encoding of 'origin'
# ---------------------------------------------------------

# Machine Learning models work better with numerical values.
# get_dummies() converts the categorical 'origin' column
# into separate 0/1 columns.

cData = pd.get_dummies(cData, columns=['origin'])

print(cData)

# We now get columns such as:
# origin_American
# origin_asia
# origin_europe
#
# 1 → car belongs to that category
# 0 → car does not belong to that category


# ---------------------------------------------------------
# 5. Check the horsepower column
# ---------------------------------------------------------

# Check the data types of all columns.
# horsepower is expected to be numeric,
# but it is currently an object/string type.
cData.dtypes


# ---------------------------------------------------------
# 6. Find invalid values in horsepower
# ---------------------------------------------------------

# horsepower contains '?' in some rows.
# '?' is a string, so pandas treats the whole column
# as an object instead of a numerical column.

# isdigit() checks whether each value contains only digits.
# True  → valid number
# False → invalid value such as '?'

hpIsDigit = pd.DataFrame(
    cData.horsepower.str.isdigit()
)

# Display rows where horsepower is NOT a valid number.
cData[hpIsDigit['horsepower'] == False]


# ---------------------------------------------------------
# 7. Replace '?' with NaN
# ---------------------------------------------------------

# '?' represents a missing/unknown horsepower value.
# Replace it with NaN (Not a Number),
# which pandas recognizes as a missing value.

cData = cData.replace('?', np.nan)

print(cData)


# Check the rows that originally contained invalid horsepower.
cData[hpIsDigit['horsepower'] == False]


# ---------------------------------------------------------
# 8. Convert horsepower from object → float
# ---------------------------------------------------------

# Now that '?' has been replaced by NaN,
# horsepower can be converted into a numerical column.

cData['horsepower'] = cData['horsepower'].astype(float)


# ---------------------------------------------------------
# 9. Find the median of each numerical column
# ---------------------------------------------------------

# Median gives the middle value of a column.
# It is useful for filling missing numerical values
# and is generally less affected by outliers than the mean.

cData.median()


# ---------------------------------------------------------
# 10. Fill missing values using the median
# ---------------------------------------------------------

# Replace missing (NaN) values with the median
# of their respective columns.

cData = cData.fillna(cData.median())

print(cData)


# Another way to do the same thing:
#
# medianFiller = lambda x: x.fillna(x.median())
# cData = cData.apply(medianFiller, axis=0)


# ---------------------------------------------------------
# 11. Convert horsepower to float64
# ---------------------------------------------------------

# This is another way to explicitly convert
# horsepower into a floating-point numerical column.

# cData['horsepower'] = cData['horsepower'].astype('float64')


# ---------------------------------------------------------
# 12. Convert One-Hot Encoded columns to integers
# ---------------------------------------------------------

# get_dummies() may create boolean (True/False) columns.
# We convert them into integers:
#
# True  → 1
# False → 0

origin_cols = [
    'origin_American',
    'origin_asia',
    'origin_europe'
]

cData[origin_cols] = cData[origin_cols].astype(int)
print(cData)


