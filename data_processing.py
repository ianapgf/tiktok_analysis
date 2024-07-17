import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from textblob import TextBlob

class DataProcessor:
    @staticmethod
    def load_data(csv_path):
        try:
            df = pd.read_csv(csv_path)
            return df
        except Exception as e:
            raise RuntimeError(f"Error loading data from {csv_path}: {e}")

    @staticmethod
    def preprocess_data(df):
        try:
            df = df.drop(columns=['URL', 'Username'])
            df['Hashtags'] = df['Hashtags'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0)
            df['Bio_Sentiment'] = df['Bio'].apply(lambda x: TextBlob(x).sentiment.polarity if pd.notnull(x) else 0)
            df = df.drop(columns=['Bio'])
            df = df.fillna(df.mean())

            X = df.drop(columns=['Followers'])
            y = df['Followers']

            scaler = StandardScaler()
            X = scaler.fit_transform(X)

            return X, y
        except Exception as e:
            raise RuntimeError(f"Error preprocessing data: {e}")
