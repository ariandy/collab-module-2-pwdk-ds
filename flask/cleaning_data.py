import pandas as pd
import numpy as np
import seaborn as sns

def data_covid():
    df = pd.read_csv('../datasets/accumulate_by_country.csv')
    return df.fillna(0)

def cleaned_covid_data():
    df = pd.read_csv('../datasets/stage-1.csv')
    return df

def top15(feature):
    feature = feature.capitalize()
    df = data_covid().sort_values(by=feature, ascending=False).head(10)
    return df[['Country_Region', feature]]
