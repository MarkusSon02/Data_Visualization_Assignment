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

# Save the result
df_rome.to_excel('results/question1_results/rome_hotels.xlsx', index=False)

# Compute summary statistic
df_rome['distance'] = pd.to_numeric(df_rome['distance'], errors='coerce')
df_rome = df_rome.dropna(subset=['distance', 'price'])  # Drop rows with missing values
summary_stats = df_rome[['distance', 'price']].describe()
summary_stats.reset_index()
summary_stats.to_excel('results/question1_results/summary_statistics.xlsx')

# Distance Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_rome['distance'], bins=20, edgecolor='black')
plt.title('Distance Histogram: Absolute Frequency (Count)')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.savefig('results/question1_results/distance_histogram.png')
plt.close()


# Price Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_rome['price'], bins=20, edgecolor='black')
plt.title('Price Histogram: Absolute Frequency (Count)')
plt.xlabel('Price (US dollars)')
plt.ylabel('Frequency')
plt.savefig('results/question1_results/price_histogram.png')
plt.close()