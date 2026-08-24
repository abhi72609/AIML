import pandas as pd

orders = pd.read_csv(r'C:\Users\hp\Desktop\Coding\AIML\2_pandas\orders.csv')
products = pd.read_csv(r'C:\Users\hp\Desktop\Coding\AIML\2_pandas\products.csv')

print(orders.head())
print(orders.shape)
print(products.head())
print(products.shape)



# Sample DataFrames
samples_orders = pd.DataFrame({
    'product_id': ['P001', 'P002', 'P003'],
    'user_id': ['U001', 'U002', 'U003'],
    'review_id': ['R001', 'R002', 'R003']
})

samples_products = pd.DataFrame({
    'product_id': ['P001', 'P002', 'P004'],
    'product_name': ['Product A', 'Product B', 'Product D'],
    'category': ['Category 1', 'Category 2', 'Category 3']
})

# Inner Join Example
inner_join = pd.merge(samples_orders, samples_products, on='product_id', how='inner')
print("Inner Join:")
print(inner_join)


# Outer Join Example
outer_join = pd.merge(samples_orders,samples_products, on='product_id', how='outer')
print("\nOuter Join:")
print(outer_join)


# Performing a Left Join to merge orders with product details
df = pd.merge(orders, products, on='product_id', how='left')

# Displaying the result
print("Best Join (Left Join) for Our Use Case:")
print(df.head())

print(df['review_title'].head())


# Now, we have a dataset with the column `review_title`. We want to convert this data into `Uppercase`.
def uppercase_title(title):
    return title.upper()

df['review_title_uppercase'] = df['review_title'].apply(uppercase_title)
print(df['review_title_uppercase'].head())
print()
# This operation can also be performed using a lambda function.
orders['review_title_uppercase'] = orders['review_title'].apply(lambda x: x.upper())
print(df['review_title_uppercase'].head())
print()
print(df['discounted_price'].head())
print(df['actual_price'].head())


def extract_price(price_str):
    try:
        return float(str(price_str).replace('₹', '').replace(',', ''))
    except ValueError:
        return None

# Apply the function to the 'actual_price' and 'discounted_price' columns
df['actual_price'] = df['actual_price'].apply(extract_price)
df['discounted_price'] = df['discounted_price'].apply(extract_price)

print(df['discounted_price'].head())
print(df['actual_price'].head())

# Define a function to calculate the effective discount percentage
def calculate_discount_percentage(row):
    return ((row['actual_price'] - row['discounted_price']) / row['actual_price']) * 100

# Apply the function along rows (axis=1)
df['calculated_discount'] = df.apply(calculate_discount_percentage, axis=1)

# Display the result
print("Products DataFrame with Calculated Discounts:")
df[['product_name', 'actual_price', 'discounted_price', 'calculated_discount']].head()


# Define aggregate functions to calculate max and min
def max_rating(series):
    return series.max()

def min_rating_count(series):
    return series.min()

# Apply the functions across columns
rating_stats = products[['rating', 'rating_count']].apply([max_rating, min_rating_count])

# Display the result
print("Rating Statistics:")
print(rating_stats)



#   GROUPING IN PANDAS

# 1. Group-Based Aggregations


# Group by a Single Column
# Example 1: Group by 'category' and calculate the average 'discounted_price'
avg_discounted_price = df.groupby('category')['calculated_discount'].mean()

# Display the results
print("Average Discounted Percentage by Category:")
print(avg_discounted_price)


# Count of products per user
# Example:
count_product_user = df.groupby('user_name')['product_name'].count()
print(count_product_user[:10])



#  Maximum and Minimum Rating Count by Category and Product Name
rating_stats = df.groupby(['category', 'product_name'])['rating_count'].agg(['max', 'min'])
print(rating_stats[:10])


# 2. Group-Based Filtering

# Filter Categories with Average Rating equal or above 4
categories_high_rating = df.groupby('category')['rating'].mean().loc[lambda x: x >= 4]
print("Categories with High Average Rating (Above 4):")
print(categories_high_rating)


# Filter Users Who Have Written More Than 15 Reviews
users_with_many_reviews = df.groupby('user_id').filter(
    lambda group: group['review_id'].count() > 15
)
print(users_with_many_reviews)


# 3. Group-Based Apply

# Group-based apply with a custom function
def avg_price_diff(group):
    # We handle potential missing data
    avg_actual = group['actual_price'].mean()
    avg_discounted = group['discounted_price'].mean()
    return avg_actual - avg_discounted

# Apply this function to each group (category) in df
price_diff_by_category = df.groupby('category').apply(avg_price_diff)

print(price_diff_by_category)

#  using .apply()
def my_aggregations(group):
    return pd.Series({
        'mean_rating': group['rating'].mean(),
        'min_discounted_price': group['discounted_price'].min(),
        'max_discounted_price': group['discounted_price'].max()
    })

# Apply custom function after grouping by 'category'
stats_by_category = df.groupby('category').apply(my_aggregations)

print(stats_by_category)


# Creating a new column during groupby apply, then filtering with .loc
def add_review_status(group):
    # Create a new column in each group based on the rating
    group['review_status'] = group['rating'].apply(
        lambda x: 'Good' if x is not None and x > 4.2 else 'Not Good'
    )
    return group

# We group by 'category', and use group_keys=True (this ensures the group labels are preserved)
df_with_status = df.groupby('category', group_keys=True).apply(add_review_status)
print(df_with_status)


filtered_df = df_with_status.loc[df_with_status['review_status'] == 'Good']

print(filtered_df.head(10))



# Series and DataFrame Output from Groupby
df = pd.DataFrame({
    "region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "score": [85, 90, 78, 88, 92, 95, 80, 84],
    "sales": [200, 250, 180, 220, 210, 260, 190, 230]
})

print(df.groupby("region")["score"].mean())