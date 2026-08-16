# Unique Value and Value Count
import pandas as pd
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\2_pandas\\zomato_dataset.csv')

print(df.shape)
print(df.info())

# Finding unique values in the 'location' column
unique_locations = df["location"].unique()
print(unique_locations)

# Using nunique()
number_of_unique_locations = df["location"].nunique()
print(number_of_unique_locations)

# Counting occurrences of each unique value
location_counts = df["location"].value_counts()
print(location_counts)




# Working with Both Rows and Columns
# Using .iloc for Rows and Columns
# Select the first two rows and the first two columns
df.iloc[0:2, 0:2]

# Select the last two rows and the last column
df.iloc[-2:, -1]

# Using .iloc to Modify Data 
# Example DataFrame
data = {
    "Restaurant": ["R1", "R2", "R3", "R4"],
    "Votes": [120, 240, 150, 80],
    "Rating": [4.1, 4.5, 3.9, 4.0]
}

sample_df = pd.DataFrame(data)

# Assigning new values to multiple rows and columns
sample_df.iloc[1:3, 1:3] = [[300, 4.7], [180, 4.2]]

print("DataFrame after modifying rows and columns:")
print(sample_df)




# Using .loc to Select Rows and Columns
#create a new column to keep track of flags - initially set it as 1 for all restaurants
df['flag'] = 1

# Setting 'Restaurant' as the index
df_explicit = df.set_index("name")

# Select specific rows ('R2' and 'R3') and specific columns ('flag')
print(df_explicit.loc[["Jalsa", "Grand Village"], ["flag"]])
print("==="*10)

# Updating the 'flag' for restaurant 'Jalsa.'
df_explicit.loc["Jalsa", "flag"] = 0
print("Updated DataFrame:")
print(df_explicit)