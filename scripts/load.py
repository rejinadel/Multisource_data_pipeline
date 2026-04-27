import pandas as pd
def load_data(df):
    df = df.to_csv("data/processed/books.csv")
    print("Data converted successfully")