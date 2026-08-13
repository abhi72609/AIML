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
print(df.head())
print(df.tail())
print(df.tail(2))