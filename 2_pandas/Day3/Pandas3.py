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