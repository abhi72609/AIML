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

print(df.info())
print(df.describe())

# Basic Operations on Columns
# Dot notation
rating = df.rate  
print(rating)

# Bracket notation
costs = df["approx_cost(for two people)"]  
print(costs)

#accessing multiple columns
df[['approx_cost(for two people)', 'rate' ]]  

# Renaming columns
df = df.rename(columns={"approx_cost(for two people)":'cost_for_two',"votes": "Total_Votes", "rate": "Ratings"})

# Displaying renamed DataFrame
print(df.head())



# Adding a new column
df["only_rating"] = df["Ratings"].str[:-2]
print(df["only_rating"])
# It is expected to fail! As you can see, the rating is still in object type. We need to convert it into a float type.
# df["only_rating"] = df["only_rating"].astype(float)
# print(df["only_rating"])
# It is failing because it looks like there is an 'N' in the ratings column, which cannot be converted into a float.

# Option 1
# Replacing certain values in object type columns
df["only_rating"] = df["only_rating"].replace('N', np.nan)
df["only_rating"] = df["only_rating"].astype(float)
print(df["only_rating"])

# Option 2
# Use pd.to_numeric with errors='coerce'
df["only_rating"] = pd.to_numeric(df["only_rating"], errors='coerce')
print(df["only_rating"])


print(df["cost_for_two"])
df["cost_for_two"] = pd.to_numeric(df["cost_for_two"].str.strip("'\""), errors="coerce")
print(df["cost_for_two"])


# Adding a new column
df['cost_for_one']  = df['cost_for_two'] / 2
print(df['cost_for_one'])


df["is_good"] = df["only_rating"] > 4
print(df["is_good"])


# Unique Values in a Column
# Finding unique values in the 'location' column
unique_locations = df["location"].unique()
print(unique_locations)



# Value Counts in a Column

# you might want to find out which are the most popular locations that people order from/ dine in
# How can Zomato's data team count the number of restaurants in each unique location in the
# Bangalore dataset to identify the most popular dining or ordering areas?


# Counting occurrences of each unique value
location_counts = df["location"].value_counts()
print(location_counts)

# Which is the most ordered restaurant in the dataset?
restaurant_order_counts = df["name"].value_counts()
print(restaurant_order_counts)

# Which type of listing (e.g., delivery, dine-out, etc.) is the most common?
listing_counts = df['listed_in(type)'].value_counts()
print(listing_counts)