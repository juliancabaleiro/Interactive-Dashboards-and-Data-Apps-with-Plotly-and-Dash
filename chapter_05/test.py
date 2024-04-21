import dash
from dash import html
from dash import dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pandas as pd
from dash.exceptions import PreventUpdate

poverty = pd.read_csv('data\poverty.csv')
gini= "GINI index (World Bank estimate)"
gini_df=poverty[poverty[gini].notna()]


a=[{"label":country,
    "value":country} 
    for country in gini_df["Country Name"].unique()]
print(type(a))
print(type(a[0]))

for i in a:
    print(i)