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



event_a_union_b = sachin_data[
    (sachin_data['runs'] > 50) |
    (sachin_data['Won'] == True)
]

p_a_union_b_direct = len(event_a_union_b) / total_matches

# Compare both:
# P_A_union_B (from formula) should equal p_a_union_b_direct (from dataset)
# Both should give the same result.




#  Multiplication Rule

## What is the probability that Sachin Tendulkar scored more than 50 runs and India won the match in his ODI career?
# Event A: Sachin scored > 50 runs
P_A = len(event_A) / total_matches

# Conditional probability: P(B | A)
conditional_data = sachin_data[sachin_data['runs'] > 50]
P_B_given_A = len(conditional_data[conditional_data['Won'] == True]) / len(event_A)

# Applying the multiplication rule
P_A_intersection_B = P_A * P_B_given_A

print(f"Probability of scoring > 50 runs and India winning: {P_A_intersection_B:.4f}")




#What is the marginal probability that Sachin Tendulkar scored a century, and what is the joint probability
# that he scored more than 50 runs and hit at least one six in an ODI match?

# Marginal probability: Sachin scored a century
event_C = sachin_data[sachin_data['century'] == True]
P_C = len(event_C) / total_matches

# Joint probability: Sachin scored > 50 runs and hit at least 1 six
event_D = sachin_data[(sachin_data['runs'] > 50) & (sachin_data['sixes'] > 0)]
P_D = len(event_D) / total_matches

print(f"Marginal Probability of Sachin scoring a century: {P_C:.4f}")
print(f"Joint Probability of scoring > 50 runs and hitting at least 1 six: {P_D:.4f}")