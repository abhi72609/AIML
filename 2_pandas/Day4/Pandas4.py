import pandas as pd

df= pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\2_pandas\\df_amazon.csv')
print(df.head(10))


missing_values = df.isna()
print(missing_values)

# To know the count of null values for each column in large dataset/dataframe - .sum():
missing_summary = df.isna().sum()
print(missing_summary)

# Use .dropna() to remove rows or columns with missing values.
# Drop rows with any missing values
cleaned_data = df.dropna()
print(cleaned_data.isna().sum())


# Use .fillna() to replace missing values with a specific value, such as the mean or median.


# Example : Fill missing ratings with the column mean
mean_rating = df['rating'].mean()
df['rating_filled'] = df['rating'].fillna(mean_rating)
print(f"Filling missing values in rating column with {mean_rating}")
print(df[["rating", 'rating_filled']].isna().sum())


# Example : Fill missing 'category' values with "Unknown"
df['category_filled'] = df['category'].fillna('Unknown')
print(df['category_filled'].value_counts())
print("==="* 10)
print(df['category'].value_counts())


# # Example : Fill missing 'calculated_discount' values with 0
df['calculated_discount_filled'] = df['calculated_discount'].fillna(0)
print(df[['product_name', 'calculated_discount', 'calculated_discount_filled']].head())



# Melting, Pivoting, and Binning


# 1. Melting with pd.melt

# Melt discounted_price and actual_price into a single column
melted_prices = pd.melt(
    df,
    id_vars=['product_id', 'product_name', 'category'],  # columns to keep
    value_vars=['discounted_price', 'actual_price'],      # columns to unpivot
    var_name='price_type',                                # new column name for variable
    value_name='price'                                    # new column name for value
)
print(melted_prices.head())


# Example 2: Melt rating and rating_count together
melted_ratings = pd.melt(
    df,
    id_vars=['product_id', 'user_id', 'category'],  # columns to keep
    value_vars=['rating', 'rating_count'],          # columns to unpivot
    var_name='rating_metric',
    value_name='value'
)
print(melted_ratings.head())


# 2. Pivoting with pivot_table



data = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\2_pandas\\Pfizer_1.csv')
print(data)



# Example : Pivot table for average rating by category and product name
pivot_avg_rating = pd.pivot_table(
    df,
    index='category',
    columns='product_name',
    values='rating',
    aggfunc='mean'
)

print(pivot_avg_rating)


# Example : Pivot table for total rating count by user and category
pivot_rating_count = pd.pivot_table(
    df,
    index='user_id',
    columns='category',
    values='rating_count',
    aggfunc='sum',
    fill_value=0
)

print(pivot_rating_count)

# 3. Binning with pd.cut

print(df['actual_price'].min())
print(df['actual_price'].max())

# Example: Bin actual prices into price ranges
price_bins = pd.cut(
    df['actual_price'],
    bins= [39, 5000, 20000, 50000, 139900],
    labels=['Low', 'Medium', 'High', 'Very High']
)
df['price_range'] = price_bins

print(df['price_range'])


# Example : Bin ratings into intervals
rating_bins = pd.cut(
    df['rating'],
    bins=[0, 2, 3.5, 4.5, 5],
    labels=['Poor', 'Average', 'Good', 'Excellent']
)
df['rating_category'] = rating_bins
print(df['rating_category'])




# String Methods


# Example: Check if 'about_product' contains the word 'durable'
df['contains_durable'] = df['about_product'].str.contains('durable', case=False, na=False)
print(df['contains_durable'])

# Filter products based on whether they contain sugar — useful for dietary analysis or product labeling.
df["contains_sugar"] = df["about_product"].str.contains("sugar", case=False, na=False)
print(df["contains_sugar"].sum())

# Extracting QID from product_link
print(df['product_link'][0])


# Example: Extract QID from 'product_link' using .split()
def extract_qid(link):
    # Split on 'qid=' and take the part after it
    qid_part = link.split('qid=')[-1]
    # Further split by '&' to isolate the QID
    return qid_part.split('&')[0] if 'qid=' in link else None

# Apply the function to extract QID
df['product_qid'] = df['product_link'].apply(extract_qid)

# Display results
print("Data with Extracted QID:")
print(df[['product_link', 'product_qid']].head())




# DateTime in pandas

# 1. Convert Strings to datetime
df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])
print(df.info())

# Example 1: Extract week number
df['week_number'] = df['order_timestamp'].dt.isocalendar().week

# Example 2: Extract day of the week
df['day_name'] = df['order_timestamp'].dt.day_name()

# Example 3: Extract year and month
df['year'] = df['order_timestamp'].dt.year
df['month'] = df['order_timestamp'].dt.month

# Display results
print("Data with DateTime Components Extracted:")
print(df[['order_timestamp', 'week_number', 'day_name', 'year', 'month']].head())



df['month_year'] = df['order_timestamp'].dt.strftime('%B %Y')
print(df['month_year'])