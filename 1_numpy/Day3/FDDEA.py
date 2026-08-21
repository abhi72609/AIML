import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

result = array_2d + scalar
print("Array:\n", array_2d)
print("---"* 10)

print("adding Scalar:", scalar)
print("---"* 10)

print("Result after broadcasting:\n", result)


# Case 2: if one array is 1D and other is higher-dimensional , Broadcasting will expand the 1D array
# Broadcasting a 1D array to a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([10, 20, 30])

result = array_2d + array_1d

print(f"{array_2d} + {array_1d} =")
print("---"* 10)
print(result)



# Case 3: Column and Row Matrices
# Column matrix (3x1) and row matrix (1x3)
col_matrix = np.array([[1], [2], [3]])
row_matrix = np.array([[10, 20, 30]])

result = col_matrix + row_matrix

print(f"{col_matrix} + {row_matrix} =")
print("---"* 10)
print(result)


# Broadcasting in 2D Arrays
# Example: Compatible shapes
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[10], [20]])

# Broadcasting works
result = array1 + array2

print("Array 1:\n", array1)
print("---"* 10)

print("Array 2:\n", array2)
print("---"* 10)

print("Result:\n", result)

# Example: Incompatible shapes
# This is expected to fail!
# array1 = np.array([[1, 2, 3], [4, 5, 6]])
# array2 = np.array([[10, 20]])

# result = array1 + array2
# result


# Using np.tile()
# Example: Explicit broadcasting with np.tile
array1 = np.array([[1, 2, 3]])
array2 = np.array([[10], [20], [30]])

# Use np.tile to match shapes
array1_tiled = np.tile(array1, (3, 1))
print(array1_tiled)

# Perform addition
result = array1_tiled + array2
print("Result:\n", result)


# Vectorization


# When working with arrays, applying a Python function directly to a NumPy array often leads to errors.
# Example: Apply a custom function to the 'rate' column
def categorize_rating(rating):
    "Categorize ratings into high or low."""
    if rating >= 4.0:
        return "High"
    else:
        return "Low"
# Attempt to apply the function directly
# This is expected to fail!
# categorized_ratings = categorize_rating(numeric_data[:, 0])  # 'rate' column
# print(categorized_ratings)


# Vectorize the categorize_rating function
vectorized_categorize_rating = np.vectorize(categorize_rating)
# print(vectorized_categorize_rating)
# Apply the vectorized function to the 'rate' column
# numeric_data
numeric_data = np.arange(11,20).reshape(3,3)
categorized_ratings = vectorized_categorize_rating(numeric_data[:, 0])

# Display a sample of the categorized ratings
print("Categorized Ratings (sample):", categorized_ratings[:10])

# Define a function to calculate the discounted cost
def discount_cost(rate, cost):
    "Apply a 10% discount if the rating is 4.0 or higher."""
    if rate >= 4.0:
        return cost * 0.9
    else:
        return cost

# Vectorize the discount_cost function
vectorized_discount_cost = np.vectorize(discount_cost)

# Apply the vectorized function to 'rate' and 'approx_cost(for two people).'
discounted_costs = vectorized_discount_cost(numeric_data[:, 0], numeric_data[:, 2])

# Display a sample of the discounted costs
print("Discounted Costs (sample):", discounted_costs[:10])



# Split

# Splitting a 1D Array
array_1d = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 sections
split_1d = np.split(array_1d, 3)

print("Original Array:", array_1d)
print("Splits:", split_1d)


# Splitting a 2D Array
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

# Split into 2 along axis=1 (columns)
split_2d = np.split(array_2d, 2, axis=1)

print("Original Array:\n", array_2d)
print("=="*10)
print("Splits:")
for part in split_2d:
    print(part)



# Horizontal Splitting with np.hsplit()
hsplit_2d = np.hsplit(array_2d, 2)

print("Original Array:\n", array_2d)
print("=="*10)
print("Horizontal Splits:")
for part in hsplit_2d:
    print(part)


# Vertical Splitting with np.vsplit()
vsplit_2d = np.vsplit(array_2d, 2)

print("Original Array:\n", array_2d)
print("Vertical Splits:")
for part in vsplit_2d:
    print(part)



# Custom Splits with Indices
custom_split = np.split(array_1d, [2, 5])

print("Original Array:", array_1d)
print("Custom Splits:", custom_split)




# Stacking
# Vertical Stacking with np.vstack()
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Stack vertically
vstack_result = np.vstack([array1, array2])

print("Array 1:", array1)
print("Array 2:", array2)
print("Vertical Stack:\n", vstack_result)



# Horizontal Stacking with np.hstack()
array4 = np.array([[1], [2], [3]])
array5 = np.array([[4], [5], [6]])
print("Array 4 shape:", array4.shape)
# Stack horizontally
hstack_result = np.hstack([array4, array5])

print("Array 4:\n", array4)
print("Array 5:\n", array5)
print("Horizontal Stack:\n", hstack_result)