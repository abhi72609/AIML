# Unique Value and Value Count
import pandas as pd
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\2_pandas\\zomato_dataset.csv')

print(df.shape)
print(df.info())

# Finding unique values in the 'location' column
unique_locations = df["location"].unique()
print(unique_locations)
