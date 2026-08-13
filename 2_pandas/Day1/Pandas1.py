import pandas as pd
import numpy as np

# Creating Series from numpy arrays ( highlight that pandas is implemented using numpy)
votes = np.array([120, 240, 150])
ratings = np.array([4.1, 4.5, 3.9])
restaurants = np.array(['R1', 'R2', 'R3'])

votes_series = pd.Series(votes, index=['R1', 'R2', 'R3'], name='Votes')
print(votes_series)

ratings_series = pd.Series(ratings, index=['R1', 'R2', 'R3'], name='Ratings')
print(ratings_series)


data = {
    "Restaurant": ["R1", "R2", "R3"],
    "Votes": [120, 240, 150],
    "Rating": [4.1, 4.5, 3.9]
}
df = pd.DataFrame(data)
print(df)


df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\2_pandas\\zomato_dataset.csv')
# print(df.head())
# print(df.tail())
# print(df.tail(2))

# Basic Operations in rows

# Slicing Rows
# iloc - Slicing based on implicit integer indices.
print(df.iloc[0]) 
print(df.iloc[1:4])  
# How can Zomato's data team sample every third restaurant from the second to the ninth entry in the
# Bangalore dataset to explore a subset of restaurant data?
print(df.iloc[1:9:3])




df_explicit = df.set_index("name")
print(df_explicit)
# loc - Slicing based on explicit labels.
print(df_explicit.loc["Jalsa"])
print(df_explicit.loc[["Jalsa", "Tuk-Tuk"]])

# You can also reset the index to get back the original df.
print(df_explicit.reset_index())

# We can drop the index altogether.
print(df_explicit.reset_index(drop=True))