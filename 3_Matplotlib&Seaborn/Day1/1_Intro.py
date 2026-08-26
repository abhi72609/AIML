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