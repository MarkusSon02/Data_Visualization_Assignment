import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
df_features = pd.read_csv('data/hotels-europe/clean/hotels-europe_features.csv')
df_price = pd.read_csv('data/hotels-europe/clean/hotels-europe_price.csv')

# Filter for Rome hotels
df_rome_features = df_features[df_features['city'] == 'Rome']

# Perform inner join on 'hotel_id'
df_rome = pd.merge(df_rome_features, df_price, on='hotel_id', how='inner')

# Save or display the result
df_rome.to_csv('rome_hotels_inner_join.csv', index=False)

# Step 1: Create a Data Table (Summary Statistics)
df_rome['distance'] = pd.to_numeric(df_rome['distance'], errors='coerce')
df_rome = df_rome.dropna(subset=['distance', 'price'])  # Drop rows with missing values
summary_stats = df_rome[['distance', 'price']].describe()
print(summary_stats)

# Step 2: Visualize Distributions (Histograms for Distance and Price)
# 1. Absolute Frequency Histogram (Count)
# ====================================
plt.figure(figsize=(7, 5))
plt.hist(df_rome['distance'], bins=20, edgecolor='black')
plt.title('Distance Histogram: Absolute Frequency (Count)')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.show()

# ====================================
# 2. Relative Frequency Histogram (Percent)
# ====================================
plt.figure(figsize=(7, 5))
plt.hist(df_rome['distance'], bins=20, edgecolor='black', weights=np.ones(len(df_rome['distance'])) / len(df_rome['distance']))
plt.title('Distance Histogram: Relative Frequency (Percent)')
plt.xlabel('Distance (miles)')
plt.ylabel('Percent')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.1f}%'))
plt.show()


def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)  # 25th percentile
    Q3 = df[column].quantile(0.75)  # 75th percentile
    IQR = Q3 - Q1                   # Interquartile range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound


# Outliers in Distance
distance_outliers, dist_lower, dist_upper = detect_outliers_iqr(df_rome, 'distance')
print("Distance Outliers:\n", distance_outliers[['distance', 'price']])

# Outliers in Price
price_outliers, price_lower, price_upper = detect_outliers_iqr(df_rome, 'price')
print("\nPrice Outliers:\n", price_outliers[['distance', 'price']])

# ====================================
# Step 3: Summary and Handling Outliers
# ====================================
print("\nHandling Outliers:")
print(f"For Distance: Lower Bound = {dist_lower}, Upper Bound = {dist_upper}")
print(f"For Price: Lower Bound = {price_lower}, Upper Bound = {price_upper}")