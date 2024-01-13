import pandas as pd

df1 = pd.read_csv('output.csv')

# Load the second CSV file
df2 = pd.read_csv('SpotifyFeatures.csv')

# Merge the dataframes based on the 'track id' column
merged_df = pd.merge(df1, df2, on='track_id', how='inner')
merged_df = merged_df.drop_duplicates(subset=['track_id','genre'])
merged_df.to_csv('merged_file.csv', index=False)