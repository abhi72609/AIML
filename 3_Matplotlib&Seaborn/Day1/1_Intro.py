# Introduction to Data Visualization with Matplotlib and Seaborn
import pandas as pd
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\3_Matplotlib&Seaborn\\amazon_data.csv')


import seaborn as sns
import matplotlib.pyplot as plt


# Univariate Data Visualization - 1  Variable Analysis


# Histogram for 'rating'
print(plt.figure(figsize=(8, 6)))
sns.histplot(data=df, x='rating', kde=False, color='skyblue')

# Styling Tip 💡
# Add a vertical line for the mean rating
mean_rating = df['rating'].mean()
print(plt.axvline(mean_rating, color='red', linestyle='--', label=f"Mean: {mean_rating:.2f}"))

print(plt.title("Distribution of Ratings", fontsize=16))
print(plt.xlabel("Rating", fontsize=12))
print(plt.ylabel("Frequency", fontsize=12))
print(plt.legend())
print(plt.show())


# Equivalent version in Matplotlib:
print(plt.figure(figsize=(8, 6)))
print(plt.hist(df['rating'].dropna(), bins=10, color='skyblue'))
print(plt.axvline(mean_rating, color='red', linestyle='--', label=f"Mean: {mean_rating:.2f}"))
print(plt.title("Distribution of Ratings"))
print(plt.xlabel("Rating"))
print(plt.ylabel("Frequency"))
print(plt.legend())
print(plt.show())



# Visualization Goal: Bar Plot (Categorical)
print(plt.figure(figsize=(8, 6)))
sns.countplot(data=df, x='category', palette='coolwarm')

# Styling Tip 💡
# Rotate the x-axis labels for better readability
print(plt.xticks(rotation=45))

print(plt.title("Count of Products by Category", fontsize=16))
print(plt.xlabel("Category", fontsize=12))
print(plt.ylabel("Count", fontsize=12))
print(plt.show())


# Equivalent version in Matplotlib:
categories = df['category'].value_counts()

print(plt.figure(figsize=(8, 6)))
print(plt.bar(categories.index, categories.values, color='skyblue'))
print(plt.xticks(rotation=45))
print(plt.title("Count of Products by Category"))
print(plt.xlabel("Category"))
print(plt.ylabel("Count"))
print(plt.show())



# Visualization Goal: KDE (Kernel Density Estimate) Plot
print(df['calculated_discount'])

print(plt.figure(figsize=(8, 6)))
sns.histplot(data=df, x='calculated_discount', color='green', kde=True)

print(plt.title("Distribution of calculated_discount of Amazon", fontsize=16.5))
print(plt.xlabel("calculated_discount", fontsize=12))
print(plt.ylabel("Frequency", fontsize=12))
print(plt.legend())
print(plt.show())


print(plt.figure(figsize=(8, 6)))
sns.kdeplot(data=df, x='discounted_price', shade=True, color='purple')

# Styling Tip 💡
# Add a vertical grid for better readability
print(plt.grid(axis='x', linestyle='--', alpha=0.7))

print(plt.title("KDE Plot of Discounted Prices", fontsize=16))
print(plt.xlabel("Discounted Price", fontsize=12))
print(plt.ylabel("Density", fontsize=12))
print(plt.show())

  


# Bivariate Plots (Two Variables)

x = [1,2,3,4,5,6,7]
y = [100,340,120,450,123,567,234]
print(plt.plot(x,y))


x = [1,2,3,4,5,6,7]
y = [100,340,120,450,123,567,234]
print(plt.scatter(x,y))


# 1. Visualization Goal: Scatter Plot
# How does the discounted price of Amazon products relate to their customer ratings, and are there any high-priced products with unexpectedly low ratings?
print(plt.figure(figsize=(8, 6)))

# Styling Tip 💡
# Use alpha to handle overlapping points
sns.scatterplot(data=df, x='discounted_price', y='rating', color='teal', alpha = 0.8)

print(plt.title("Discounted Price vs. Rating", fontsize=16))
print(plt.xlabel("Discounted Price", fontsize=12))
print(plt.ylabel("Rating", fontsize=12))
print(plt.show())


print(sns.scatterplot(data=df, x='discounted_price', y='actual_price'))

print(sns.scatterplot(data=df, x='discounted_price', y='actual_price', hue='category'))


df1 = df[df['category'].isin(['Electronics','HomeImprovement'])]
print(df1)


plt.figure(figsize=(12, 9))
#plt.scatter(df1['discounted_price'],df1['actual_price'])
print(sns.scatterplot(data=df1, x='discounted_price', y='actual_price', hue="category"))
#plt.plot([10000,20000],[40000,50000])


# Visualization Goal: Line Plot

print(df[['month_year','rating_filled']])

monthly_rating = df.groupby('month_year')['rating_filled'].mean()
print(monthly_rating)

print(monthly_rating.index)

print(monthly_rating.reset_index())

monthly_rating = monthly_rating.reset_index()
print(monthly_rating)

print(monthly_rating.info())

print(pd.to_datetime(monthly_rating['month_year'],format="%B %Y"))

print(pd.to_datetime(monthly_rating['month_year']))

monthly_rating['month_year'] = pd.to_datetime(monthly_rating['month_year'], format='%B %Y')
print(monthly_rating)

# Sort the DataFrame based on 'month_year.'
monthly_rating = monthly_rating.sort_values('month_year')
print(monthly_rating)

print(monthly_rating.info())

print(monthly_rating["month_year"].dt.day)

print(monthly_rating['month_year'].dt.strftime('%B %Y'))

# How has customer satisfaction, as measured by average product ratings, changed month by month?
monthly_rating['month_year'] = monthly_rating['month_year'].dt.strftime('%B %Y')
print(monthly_rating)



import pandas as pd
import matplotlib.pyplot as plt

# Group by 'month_year' and calculate average rating
monthly_rating = df.groupby('month_year')['rating_filled'].mean().reset_index()

# Ensure 'month_year' is in datetime format
#sept - b
#September
monthly_rating['month_year'] = pd.to_datetime(monthly_rating['month_year'], format='%B %Y')

# Sort the DataFrame based on 'month_year.'
monthly_rating = monthly_rating.sort_values('month_year')

# Convert back to string for proper x-axis labels
monthly_rating['month_year'] = monthly_rating['month_year'].dt.strftime('%B %Y')

# Plot
print(plt.figure(figsize=(10, 6)))
print(plt.plot(monthly_rating['month_year'], monthly_rating['rating_filled'], marker='o', color='navy'))

# Rotate the x-axis labels and add a grid
print(plt.xticks(rotation=45))
print(plt.grid(True, linestyle='--', alpha=0.7))
#plt.grid(linestyle='--', alpha=0.7)

print(plt.title("Average Rating by Month-Year", fontsize=16))
print(plt.xlabel("Month-Year", fontsize=12))
print(plt.ylabel("Average Rating", fontsize=12))
print(plt.tight_layout())
print(plt.show())



# Group by 'month_year' and calculate average rating
monthly_rating = df.groupby('month_year')['rating_filled'].mean().reset_index()

# Ensure 'month_year' is in datetime format
#sept - b
#September
monthly_rating['month_year'] = pd.to_datetime(monthly_rating['month_year'], format='%B %Y')

# Sort the DataFrame based on 'month_year.'
monthly_rating = monthly_rating.sort_values('month_year')

# Convert back to string for proper x-axis labels
monthly_rating['month_year'] = monthly_rating['month_year'].dt.strftime('%B %Y')

# Plot
print(plt.figure(figsize=(10, 6)))
print(plt.plot(monthly_rating['month_year'], monthly_rating['rating_filled'], marker='o', color='navy'))

# Rotate the x-axis labels and add a grid
print(plt.xticks(rotation=45))
print(plt.grid(False))
print(plt.tight_layout())#"Please adjust margins so everything fits neatly within the figure."
