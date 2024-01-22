import pandas as pd

def read_data(filepath):
    """
    Reads in csv from filepath and returns dataframe for analysis.

    Inputs: 
        filepath -> str: path to csv

    Outputs:
        df -> dataframe for analysis

    """
    df = pd.read_csv(filepath)
    return df

def ingress(df):
    # TODO write docstring
    # TODO convert the birthday to datetimes
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    return df

def gender_count(df):
    # TODO write docstring
    # TODO write test
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    # TODO write docstring
    # TODO write test
    return len(df['CHILD'].unique())
