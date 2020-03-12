import pandas as pd

def date_splitter(dataframe, column): # Splits dates into month / day / year
    dataframe['Month'] = dataframe[column].dt.month
    dataframe['Day'] = dataframe[column].dt.day
    dataframe['Year'] = dataframe[column].dt.year

    return dataframe # Return new dataframe

def time_splitter(dataframe, column): # Splits times into hour / minute / second
    dataframe['Hour'] = dataframe[column].dt.hour
    dataframe['Minute'] = dataframe[column].dt.minute
    dataframe['Second'] = dataframe[column].dt.second

    return dataframe # Return new dataframe