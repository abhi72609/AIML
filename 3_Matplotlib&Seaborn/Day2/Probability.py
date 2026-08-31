
# #  Probability
import numpy as np

sachin_data  = pd.read_csv("C:\\Users\\hp\\Desktop\\Coding\\AIML\\3_Matplotlib&Seaborn\\runs,NotOut,mins,bf,fours,sixes,sr,.txt")
print(sachin_data)

print(sachin_data.info())

## What are all the distinct run totals Sachin Tendulkar has scored in his ODI career, and how many unique outcomes exist?

# Extract unique scores from the dataset
sample_space = sachin_data['runs'].unique()

# Display the sample space
print("Sample Space (Unique Runs):", sorted(sample_space))
print("Number of Unique Outcomes in the Sample Space:", len(sample_space))



# Visualizing Events with Set Operations

# Intersection (∩):
# Define events
event_A = sachin_data[sachin_data['runs'] > 50]  # Event A: Scores > 50
event_B = sachin_data[sachin_data['Won'] == True]  # Event B: India wins
# Note: True without quotes is Boolean. "True" with quotes is a string.
# Since Won is a Boolean column, we compare it with Boolean True.

# Intersection (A ∩ B)
intersection = pd.merge(event_A, event_B, how='inner')

# Display results
print("Matches where Sachin scored > 50 runs and India won:")
print(intersection[['Opp', 'Ground', 'runs', 'century']])



# Union (∪):


# Union (A ∪ B) using concatenation and dropping duplicates
union = pd.concat([event_A, event_B]).drop_duplicates()

# Display results
print("Matches where Sachin scored > 50 runs or India won:")
print(union[['Opp', 'Ground', 'runs', 'century']])

# Alternative approach using | operator directly on the DataFrame
# event_a_union_b = sachin_data[
#     (sachin_data['runs'] > 50) |
#     (sachin_data['Won'] == True)
# ]

# Note on drop_duplicates():
# Some rows may belong to both event A and event B.
# Concatenating both subsets may include those rows twice.
# drop_duplicates() removes duplicate rows.
# Without it, this behaves like SQL UNION ALL.
# With it, this behaves like SQL UNION.



# Complement (A'):

event_A_complement = sachin_data[sachin_data['runs'] < 100]  # Not a century

# Alternative using NOT operator (~)
# event_A_complement = sachin_data[~(sachin_data['runs'] >= 100)]
# The tilde (~) means NOT. It flips True to False and False to True.
# This is useful when complement is not simply a reversed inequality.

# Display results
print("Matches where Sachin did not score a century:")
print(event_A_complement[['Opp', 'Ground', 'runs', 'century']])