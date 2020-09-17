import plotly
import plotly.graph_objects as go 
import plotly.express as px
import json
import numpy as np
from cleaning_data import cleaned_covid_data
import pandas as pd

def bubble(feature, pal):
    feature = feature.capitalize()
    df = cleaned_covid_data()
    df['Date'] = pd.to_datetime(df['Date'])
    temp = df[df[feature]>0].sort_values('Country_Region', ascending=False)
    fig = px.scatter(temp, x='Date', y='Country_Region', size=feature, color=feature, height=3000,
                    color_continuous_scale=pal)
    fig.update_layout(yaxis = dict(dtick = 1))
    fig.update(layout_coloraxis_showscale=False)
    fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

# LAG PARAH !!!!!
# def map_over_time():
#     df = cleaned_covid_data()
#     df['Date'] = pd.to_datetime(df['Date'])
#     fig = px.choropleth(df, locations="Country_Region", 
#                         color=np.log(df["Confirmed"]),
#                         locationmode='country names', hover_name="Country_Region", 
#                         animation_frame=df["Date"].dt.strftime('%Y-%m-%d'),
#                         title='Cases over time', color_continuous_scale=px.colors.sequential.matter)
#     fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
#     return fig_json