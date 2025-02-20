import pandas as pd

# Load datasets
df_features = pd.read_csv('hotels-europe_features.csv')
df_price = pd.read_csv('hotels-europe_price.csv')

# Filter for Rome hotels
df_rome_features = df_features[df_features['city'] == 'Rome']

# Perform inner join on 'hotel_id'
df_rome = pd.merge(df_rome_features, df_price, on='hotel_id', how='inner')

# Save or display the result
df_rome.to_csv('rome_hotels_inner_join.csv', index=False)