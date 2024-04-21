import os
import pandas as pd

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output,Input

poverty_data=pd.read_csv("data/PovStatsData.csv")

app=dash.Dash(__name__,external_scripts=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    html.H2("Countries teste"),
    dcc.Dropdown(id="country",
                 options=[{"label": country,
                           "value":country}
                           for country in poverty_data["Country Name"].unique()]),
    html.Br(),
    html.Div(id="report")
])

@app.callback(Output(component_id="report",
                     component_property="children"),
             Input(component_id="country",
                   component_property="value"))
def display_country_report(country):
    if country is None:
        return ""
    filtered_df=poverty_data[(poverty_data["Country Name"]==country)
                              & (poverty_data["Indicator Name"]=="Population, total")]
    population= filtered_df.loc[:,"2010"].values[0]
    return [html.H3(country),
            f"The population os {country} in 2010 was {population:,.0f}."]

if __name__=="__main__":
    app.run_server(debug=True)