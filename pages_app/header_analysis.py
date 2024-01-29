import pandas as pd
import streamlit as st
import numpy as np
import json
import plotly.express as px

def ingress(df):
    # TODO write docstring
    # TODO convert the birthday to datetimes
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    df['DOB'] = pd.to_datetime(df['DOB'], format = "%d/%m/%Y", errors='coerce')
    df['AGE'] = pd.to_datetime('today').normalize() - df['DOB']
    df['AGE'] = (df['AGE'] / np.timedelta64(1,'Y')).astype('int')
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

st.title("903 Header Analysis App")

upload = st.file_uploader("Upload 903 header file")

if upload:

    df = pd.read_csv(upload)

    # with st.sidebar:
    #     ethnicities = st.sidebar.multiselect(
    #         'Select ethnicities for analysis',
    #         df['ETHNIC'].unique(),
    #         df['ETHNIC'].unique()
    #     )

    # df = df[df['ETHNIC'].isin(ethnicities)]

    df = ingress(df)
    child_pop = child_count(df)
    male, female = gender_count(df)
    average_age = round(df['AGE'].mean())


    st.write(f"The total population of children is {child_pop}.")
    st.write(f"The total number of males is {male}.")
    st.write(f"The total number of females is {female}.")
    st.write(f"The average age is {average_age}.")

    gender_bar = px.bar(df, x='SEX',
                        title="No. of children in each sex in 903 data",
                        labels={'SEX': 'Sex',
                                'count':'No. of children'
                                }
                        )
    
    ethnic_bar = px.bar(df, x='ETHNIC',
                        title="No. of children by ethnicity in 903 data",
                        labels={'ETHNIC':'Ethnicity',
                                'count':'No. of children'
                                }
                        
                        )
    
    age_histogram = px.histogram(df, x='AGE',
                                 title="No. of children by age",
                                 labels={'AGE':'Age',
                                        'count':'No. of children'
                                        }
                                 )
    
    age_sex_histogram = px.histogram(df, x='AGE', color='SEX',
                                 title="No. of children by age and sex",
                                 labels={'AGE':'Age',
                                        'SEX': 'Sex',
                                        'count':'No. of children'
                                        }
                                 )

    st.plotly_chart(gender_bar)
    st.plotly_chart(ethnic_bar)
    st.plotly_chart(age_histogram)
    st.plotly_chart(age_sex_histogram)

    st.dataframe(df)

    
