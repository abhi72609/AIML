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



# Using .loc for Conditional Updates

# Update 'Rating' for all restaurants with 'Votes' greater than 200
df_explicit.loc[df_explicit["only_rating"] < 3, "flag"] = -1



# Combining DataFrames with concat.
# Creating a second DataFrame
data2 = {
    "Restaurant": ["R5", "R6"],
    "Votes": [90, 110],
    "Rating": [3.8, 4.3]
}

df2 = pd.DataFrame(data2)

# Concatenating row-wise
combined_df = pd.concat([sample_df, df2], ignore_index=True)
print("Combined DataFrame (Row-wise):")
print(combined_df)


# Creating a DataFrame with new columns
new_columns = {
    "Delivery Time (mins)": [30, 25, 35, 20, 40, 28]
}

df_new_cols = pd.DataFrame(new_columns)

# Concatenating column-wise
final_df = pd.concat([combined_df, df_new_cols], axis=1)
print("Final DataFrame (Column-wise):")
print(final_df)



# 1. Using `.iloc` to retrieve the first two rows and the last column
print(sample_df.iloc[:2, -1])

# 2. Using `.loc` to update 'Rating' for restaurants with votes < 150
sample_df.loc[sample_df["Votes"] < 150, "Rating"] = 4.0
print(sample_df)

# 3. Adding a new row,

new_row = pd.DataFrame([["R7", 100, 3.7]], columns=sample_df.columns)
sample_df = pd.concat([sample_df, new_row], ignore_index=True)
print(sample_df)

# 4. Concatenating two DataFrames
df_with_time = pd.DataFrame({"Delivery Time (mins)": [30, 40, 20, 35, 25]})
final_combined_df = pd.concat([sample_df, df_with_time], axis=1)
print(final_combined_df)

# 5. Finding updated 'Rating' for restaurants with votes > 200
updated_ratings = final_combined_df.loc[final_combined_df["Votes"] > 200, "Rating"]
print(updated_ratings)