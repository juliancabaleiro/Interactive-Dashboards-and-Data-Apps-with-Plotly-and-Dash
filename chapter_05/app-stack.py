import dash
from dash import html
from dash import dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate
import re

poverty = pd.read_csv('data\poverty.csv')
income_share_df=poverty.filter(regex="Country Name|^year$|Income share.*?20").dropna()

income_share_df = income_share_df.rename(columns={
    'Income share held by lowest 20%': '1 Income share held by lowest 20%',    
    'Income share held by second 20%': '2 Income share held by second 20%',    
    'Income share held by third 20%': '3 Income share held by third 20%',    
    'Income share held by fourth 20%': '4 Income share held by fourth 20%',    
    'Income share held by highest 20%': '5 Income share held by highest 20%'
    }).sort_index(axis=1)

income_share_df.columns=[re.sub("\d Income share held by ", "",col).title()
                         for col in income_share_df.columns]
income_share_cols=income_share_df.columns[:-2]

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
            html.H2("Gini INdex - world Bank Data",
                    style={"textAlign":"center"}),
            dcc.Dropdown(id="income_share_country_dropdown",
                         options=[{"label":country,
                                   "value":country}
                        for country in income_share_df["Country Name"].unique()]),
            dcc.Graph(id="income_share_country_barchart")                        
])

@app.callback(Output(component_id="income_share_country_barchart",
                     component_property="figure"),
             Input(component_id="income_share_country_dropdown",
                   component_property="value"))
def plot_income_share_barchart(country):
    if country is None:
        raise PreventUpdate
    fig=px.bar(income_share_df[income_share_df["Country Name"]==country].dropna(),
                x=income_share_cols,
                y="Year",
                barmode="stack",
                height=600,
                hover_name="Country Name",
                title=f"Income share Quintiles - {country}",
                orientation="h")
    fig.layout.legend.title=None
    fig.layout.legend.orientation="h"
    fig.layout.legend.x=0.25
    fig.layout.xaxis.title="Percent of Total Income"
    return fig   

if __name__=="__main__":
    app.run_server(debug=True)