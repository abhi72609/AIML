import numpy as np
print("Hello NumPy")

import numpy as np
votes = np.array([ 775,  787,  918,   88,  166,  286, 2556,  324,  504,  402])

# Note: intentionally messy data
costs = np.array(["'800.0'" ,"'800.0'", "'800.0'", "'300.0'", "'600.0'", "'600.0'", "'600.0'", "'700.0'" ,"'550.0'", "'500.0'"])

print("Votes (Array):", votes)
print("Costs (Array):", costs)
print(type(votes))


votes * 2

# Dimensions & Shape
print("Votes array shape:", votes.shape)
print("Votes array dimensions:", votes.ndim)
print("Votes array size:", votes.size)

print("Costs array shape:", costs.shape)
print("Costs array dimensions:", costs.ndim)
print("Costs array size:", costs.size)



# Take first 5 elements of votes and costs
subset_votes = votes[:5]
subset_costs = costs[:5]

# Create a 2D array: 5 rows, 2 columns (each row: [vote_count, cost])
two_d_data = np.array([
    subset_votes,
    subset_costs
]).T  # transpose so that each row corresponds to a single restaurant

print("2D Array:\n", two_d_data)
print("Shape:", two_d_data.shape)
print("Dimensions:", two_d_data.ndim)
print("Size:", two_d_data.size)



import numpy as np

a = np.array(['1.2', '2.5', '3.6', '4.8'])
print("Type of a: ", type(a))
print("Type of elements of a: ", a.dtype)

a = a.astype(float)
print(a.dtype)

print("First 5 votes:", votes[:5])
print("First 10 costs:", costs[:10])

# 2D array slicing (two_d_data from above)
print("First 3 rows of the 2D array:\n", two_d_data[:3, :])

print("Last vote:", votes[-1])
print("Second last vote:", votes[-2])