import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sachin_data  = pd.read_csv("C:\\Users\\hp\\Desktop\\Coding\\AIML\\3_Matplotlib&Seaborn\\runs,NotOut,mins,bf,fours,sixes,sr,.txt")
print(sachin_data)


# What is the probability that Sachin Tendulkar scored more than 50 runs or India won the match in his ODI career?

# Total matches
total_matches = len(sachin_data)

# Event A: Sachin scored > 50 runs
event_A = sachin_data[sachin_data['runs'] > 50]

# Event B: India won the match
event_B = sachin_data[sachin_data['Won'] == True]

# Intersection (A ∩ B): Matches where Sachin scored > 50 runs and India won
intersection = pd.merge(event_A, event_B, how='inner')

# Probabilities
P_A = len(event_A) / total_matches
P_B = len(event_B) / total_matches
P_A_intersection_B = len(intersection) / total_matches

# Applying the addition rule
P_A_union_B = P_A + P_B - P_A_intersection_B

print(f"Probability of scoring > 50 runs or India winning: {P_A_union_B:.4f}")