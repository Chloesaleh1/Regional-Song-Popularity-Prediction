import pandas as pd
import random


df = pd.read_csv('country_wise_popularity.csv') 

def generate_dummy(row):
    acoustic_features = ['acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness',
                         'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence']
    
    random_scores = [random.random() for _ in range(len(acoustic_features))]
    
    dummy_list = list(zip(acoustic_features, random_scores))
    
    dummy_list.sort(key=lambda x: x[1], reverse = True)
    
    return dummy_list

df['dummy_column'] = df.apply(generate_dummy, axis=1)


df.to_csv('dummy_country_wise_popularity_ranked_features.csv', index=False)