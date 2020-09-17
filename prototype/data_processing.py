import pandas as pd
from datetime import datetime

def accumulate_by_country(df):
    date_now = str(datetime.utcnow())[:10]
    x = df['Country_Region'].unique()
    confirmed_arr = []
    active_arr = []
    deaths_arr = []
    recovered_arr = []
    for i in range(len(x)):
        confirmed_arr.append(df[(df['Country_Region']==x[i]) & (df['Date']==date_now)]['Confirmed'].sum())
        active_arr.append(df[(df['Country_Region']==x[i]) & (df['Date']==date_now)]['Active'].sum())
        deaths_arr.append(df[(df['Country_Region']==x[i]) & (df['Date']==date_now)]['Deaths'].sum())
        recovered_arr.append(df[(df['Country_Region']==x[i]) & (df['Date']==date_now)]['Recovered'].sum())
    print('Finish')
    d = {
            'Country_Region': x,
            'Confirmed': confirmed_arr,
            'Active': active_arr,
            'Recovered': recovered_arr,
            'Deaths': deaths_arr
        }
    d = pd.DataFrame(data=d)
    d['Case-Fatality_Ratio'] = (d['Deaths'] / d['Confirmed'])*100
    d['Case-Recovery_Ratio'] = (d['Recovered'] / d['Confirmed'])*100
    return d