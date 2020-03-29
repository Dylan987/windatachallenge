import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convert_to_int(df): # converts all numeric rows to int64
    cols = df.columns.drop('Start Time')
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

def split_df(df): # returns an array where each element is one traffic type of the data (ex. buses)
    split_arr = []
    start = 0
    end = 5670
    while (end < 40344):
        new_df = df.iloc[start:end].copy()
        convert_to_int(new_df)
        new_df['Start Time'] = pd.to_datetime(new_df['Start Time'])
        new_df.set_index(['Start Time'], inplace=True)
        split_arr.append(new_df)
        start += 5764
        end = start + 5760
    return split_arr

dorchester_data = pd.read_csv("CityOfWindsorData/Count/Dorchester Road and Huron Church Road.csv",
                              parse_dates=["Start Time"], header=10, engine='python')
malden_data = pd.read_csv("CityOfWindsorData/Count/Malden Road and Huron Church Road.csv",
                          parse_dates=["Start Time"], header=10, engine='python')
totten_data = pd.read_csv("CityOfWindsorData/Count/Totten Street and Huron Church Road.csv",
                          parse_dates=["Start Time"], header=10, engine='python')
# print(dorchester_data)

dorchester_arr = split_df(dorchester_data)
malden_arr = split_df(malden_data)
totten_arr = split_df(totten_data)

# print(dorchester_arr[0])
# for df in dorchester_arr:
#     print(df)