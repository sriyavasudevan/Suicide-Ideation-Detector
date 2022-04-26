import pandas as pd


def read_data(filename):
    df = pd.read_csv(filename)
    return df
