import pandas as pd

def preprocess_data(data):
    # Convert categorical columns to numeric
    data = pd.get_dummies(data)

    return data