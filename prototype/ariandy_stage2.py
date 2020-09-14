import numpy as np
import pandas as pd

def column_deleter(dataframe, column):
    if column in dataframe:
        dataframe.drop(column, axis=1, inplace=True)
    return dataframe

def column_extractor(dataframe, *columns):
    for i in range(len(columns)):
        column_deleter(dataframe, columns[i])
    return dataframe

def remove_zero_and_duplicated_null_on_latlong(df, lat_column, long_column):
    df = df[~df[lat_column].isna() & ~df[long_column].isna()].drop_duplicates()
    return df[(df[lat_column] != 0) & (df[long_column] != 0)].reset_index(drop=True)    

def temp_col_for_latlong_manipulation(
    df, combined, province_state, country_region,
    lat_mean='lat_mean', long_mean='long_mean'):
    df[combined] = df[province_state] + ', ' + df[country_region]
    df[lat_mean] = 0.0
    df[long_mean] = 0.0
    return df

def region_squeezer(df, combined, province_state, country_region):
    df = temp_col_for_latlong_manipulation(df, combined, province_state, country_region)
    for i in range(len(df)):
        x = df[df[combined] == df.iloc[i,4]].mean()
        df.iloc[i,5] = x.values[0]
        df.iloc[i,6] = x.values[1]
    df.Lat = df.lat_mean
    df.Long_ = df.long_mean
    df = column_extractor(df, 'lat_mean', 'long_mean', 'combined')
    return df.drop_duplicates().reset_index(drop=True)

def latlong_filler(df, ref):
    for i in range(len(ref)):
        null_catcher = ((df['Lat'].isnull()) & (df['Long_'].isnull()))
        zero_catcher = ((df['Lat']==0.0) & (df['Long_']==0.0))
        x = df[null_catcher | zero_catcher].index
        for j in x:
            cond_a = (np.isnan(df.iat[j, 4])) and (np.isnan(df.iat[j, 5]))
            cond_b = (df.iat[j, 4]==0.0) and (df.iat[j, 5]==0.0)
            if (df.iat[j, 12]==ref.iat[i, 4]):
                if cond_a or cond_b:
                    df.iat[j, 4] = ref.iat[i, 2]
                    df.iat[j, 5] = ref.iat[i, 3]
                print(j)
        print('------------> '+ str(i)+'/'+str(len(ref)-1)+' '+ref.iat[i, 4])
    print('Finish')
    return df

def latlong_filler_all_mean(df, ref):
    for i in range(len(ref)):
        x = df[df['Combined']==ref.iat[i,4]].index
        for j in x:
            if (df.iat[j, 12]==ref.iat[i, 4]):
                df.iat[j, 4] = ref.iat[i, 2]
                df.iat[j, 5] = ref.iat[i, 3]
                print(j)
        print('------------> '+ str(i)+'/'+str(len(ref)-1)+' '+ref.iat[i, 4])
    print('Finish')
    return df

def time_series_builder(df, feature):
    splitter = df.Last_Update.str.split(expand=True)
    df['Date'] = splitter[0]

    x = df[df['Country_Region']=='Mainland China'].index
    for i in x:
        df.iat[i, 2]='China'

    df.drop('Admin2', axis=1, inplace=True)
    df.drop('Last_Update', axis=1, inplace=True)
    df.drop('Combined', axis=1, inplace=True)
    element = ['Active', 'Recovered', 'Deaths', 'Confirmed', 'Incidence_Rate', 'Case-Fatality_Ratio']
    element.remove(feature)

    for i in range(len(element)):
        df.drop(element[i], axis=1, inplace=True)

    df.drop_duplicates(inplace=True)
    df = df.groupby(['Province_State', 'Country_Region', 'Lat', 'Long_', 'Date'])[feature].mean()
    df = df.unstack()
    df.columns.name = None
    df = df.fillna(0)
    return df