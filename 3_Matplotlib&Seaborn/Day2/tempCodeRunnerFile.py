print(df.loc[df['category']=="Car&Motorbike"])

# print(sns.pairplot(data=df[['discounted_price', 'actual_price', 'calculated_discount_filled', 'rating_filled']]))

# sns.pairplot(df[['rating', 'discounted_price', 'actual_price', 'calculated_discount_filled']].dropna(),
#              diag_kind='kde', corner=True, plot_kws={'alpha':0.5})
# print(plt.show())

# # Visualization Goal: Heatmap

# corr_cols = ['rating', 'discounted_price', 'actual_price', 'rating_count', 'calculated_discount']
# corr_matrix = df[corr_cols].corr()
# print(corr_matrix)


# sns.heatmap(corr_matrix)

# sns.heatmap(corr_matrix,annot=True) # annot=True means show the numerical values inside each cell of the heatmap.

# corr_cols = ['rating', 'discounted_price', 'actual_price', 'rating_count', 'calculated_discount']
# corr_matrix = df[corr_cols].corr()

# plt.figure(figsize=(8, 6))

# # Styling Tip
# # Format annotation to 2 decimal places
# sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='Blues')

# plt.title("Correlation Heatmap", fontsize=16)
# print(plt.show())



# plt.figure(figsize=(8, 6))

# # Group by rating_category and contains_durable, then compute average rating
# grouped_data = df.groupby(['rating_category', 'contains_durable'])['rating_filled'].mean().reset_index()

# sns. barplot(
#     data=grouped_data,
#     x='rating_category',
#     y='rating_filled',
#     hue='contains_durable',
#     palette='viridis'
# )

# # Styling Tip 💡
# # Add a legend title and rotate x-axis labels
# print(plt.legend(title='Durable?'))
# print(plt.xticks(rotation=45))
# print(plt.title("Average Rating by Rating Category and Durability", fontsize=16))
# print(plt.xlabel("Rating Category", fontsize=12))
# print(plt.ylabel("Average Rating", fontsize=12))
# print(plt.show())

# grouped_data = df.groupby(['category','contains_durable'])['rating_filled'].mean().reset_index()
# print(grouped_data)

# sns.barplot(data=grouped_data, x='category', y='rating_filled')
# plt.xticks(rotation=90)
# print(plt.show())

# # Hue - use to color the data points (or bars, lines, etc.) by another categorical variable, giving a quick comparison without creating separate subplots
# sns.barplot(data=grouped_data, x='category', y='rating_filled', hue='contains_durable')
# plt.xticks(rotation=90)
# print(plt.show())

# fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# # Subplot 1: Hue by 'rating_category.'
# sns. scatterplot(
#     data=df,
#     x='discounted_price',
#     y='rating_filled',
#     hue='rating_category',
#     ax=axes[0],
#     palette='coolwarm'
# )
# axes[0].set_title("Discounted Price vs. Rating (Hue: Rating Category)", fontsize=14)
# axes[0].set_xlabel("Discounted Price", fontsize=12)
# axes[0].set_ylabel("Rating", fontsize=12)

# # Subplot 2: Hue by 'price_range.'
# sns. scatterplot(
#     data=df,
#     x='discounted_price',
#     y='rating_filled',
#     hue='price_range',  # Alternatively: 'actual_price', binned, or another categorical col
#     ax=axes[1],
#     palette='Spectral'
# )
# axes[1].set_title("Discounted Price vs. Rating (Hue: Price Range)", fontsize=14)
# axes[1].set_xlabel("Discounted Price", fontsize=12)
# axes[1].set_ylabel("Rating", fontsize=12)

# plt.tight_layout()
# print(plt.show())


# monthly_rating = pd.read_csv('C:\\Users\\hp\\Desktop\\Coding\\AIML\\3_Matplotlib&Seaborn\\monthly_ratings.csv')
# print(monthly_rating)

# # 1
# plt.figure(figsize=(16,9))
# plt.subplot(2,3,1)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)
# plt.tight_layout()

# plt.subplot(2,3,2)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# plt.subplot(2,3,3)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,4)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# plt.subplot(2,3,5)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,6)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# print(plt.show())




# #2
# plt.figure(figsize=(14,9))
# plt.subplot(2,3,1)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,2)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# plt.subplot(2,3,3)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,4)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# plt.subplot(2,3,5)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,6)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# print(plt.show())




# #3
# plt.figure(figsize=(16,14))
# plt.subplot(2,3,1)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)
# plt.tight_layout()

# plt.subplot(2,3,2)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# plt.subplot(2,3,5)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(2,3,6)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)

# print(plt.show())



# #4
# plt.figure(figsize=(16,8))
# plt.subplot(1,2,1)
# sns.boxplot(data=df, x='category', y='rating', palette='Set3') # Styling Tip palette
# plt.xticks(rotation=90)

# plt.subplot(1,2,2)
# plt.bar(monthly_rating['month_year'], monthly_rating['rating_filled'], color='skyblue')
# plt.xticks(rotation=90)
# print(plt.tight_layout())




# # Stacked Plots


# # 1. Group by price_range and rating_category, and get counts
# grouped_stack = df.groupby(['price_range', 'rating_category'])['review_id'].count().unstack()

# # 2. Plot as a stacked bar
# grouped_stack.plot(
#     kind='bar',
#     stacked=True,
#     figsize=(10, 6),
#     colormap='Blues'
# )

# # Styling Tip
# plt.title("Stacked Bar Plot: Rating Categories by Price Range", fontsize=16)
# plt.xlabel("Price Range", fontsize=12)
# plt.ylabel("Number of Reviews", fontsize=12)
# plt.legend(title="Rating Category")
# plt.xticks(rotation=45)
# plt.tight_layout()
# print(plt.show())


