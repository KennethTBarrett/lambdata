import pandas as pd

def date_splitter(dataframe, column):
    # Splitting into Day / Month / Year
    dataframe['Day'] = dataframe[column].dt.day
    dataframe['Month'] = dataframe[column].dt.month
    dataframe['Year'] = dataframe[column].dt.year

    # Dropping the original column
    dataframe = dataframe.drop(columns = column)

    return dataframe # Return new version of dataframe

def time_splitter(dataframe, column):

    # Splitting into Hour / Minute / Second
    dataframe['Hour'] = dataframe[column].dt.hour
    dataframe['Minute'] = dataframe[column].dt.minute
    dataframe['Second'] = dataframe[column].dt.second

    # Dropping the original column
    dataframe = dataframe.drop(columns = column)

    return dataframe # Return new version of dataframe