import pandas as pd
import numpy as np

votes = np.array([120, 240, 150])
ratings = np.array([4.1, 4.5, 3.9])
restaurants = np.array(['R1', 'R2', 'R3'])

votes_series = pd.Series(votes, index=['R1', 'R2', 'R3'], name='Votes')
print(votes_series)

ratings_series = pd.Series(ratings, index=['R1', 'R2', 'R3'], name='Ratings')
print(ratings_series)