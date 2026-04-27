import pandas as pd
def transform_data(data):
    df = pd.DataFrame(data)
    rating_map = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5


    }

    df["rating"] = df["rating"].map(rating_map)
    df["stock"] = df["stock"].str.replace("In stock","yes")

    return df 


