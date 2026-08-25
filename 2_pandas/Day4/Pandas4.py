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
