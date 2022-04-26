import pandas as pd
import file_io as file_io


def preprocess():
    filename = "Suicide_Detection.csv"
    df = file_io.read_data(filename)
    print(df.info)
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    print(df.head(10))

