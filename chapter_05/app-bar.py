import dash
from dash import html
from dash import dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

poverty = pd.read_csv('data\poverty.csv')
gini= "GINI index (World Bank estimate)"
gini_df=poverty[poverty[gini].notna()]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
            html.H2("Gini INdex - world Bank Data",
                    style={"textAlign":"center"}),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id="gini_year_dropdown",
                                 options=[{"label":year,
                                           "value":year}
                                for year in gini_df["year"].drop_duplicates().sort_values()]),
                                dcc.Graph(id="gini_year_barchart")
                ]),
                dbc.Col([
                    dcc.Dropdown(id="gini_country_dropdown",
                                 options=[{"label":country,
                                           "value":country}
                                for country in gini_df["Country Name"].unique()]),
                    dcc.Graph(id="gini_country_barchart")
                ])
            ])
])

@app.callback(Output(component_id="gini_year_barchart",
                     component_property="figure"),
             Input(component_id="gini_year_dropdown",
                   component_property="value"))
def plor_gini_year_barchart(year):
    if not year:
        raise PreventUpdate
    df=gini_df[gini_df["year"].eq(year)].sort_values(gini).dropna(subset=[gini])
    n_countries=len(df["Country Name"])
    fig=px.bar(df,
               x=gini,
               y="Country Name",
               orientation="h",
               height=200+(n_countries*20),
               title=gini+" "+str(year))
    return fig

@app.callback(Output(component_id="gini_country_barchart",
                     component_property="figure"),
             Input(component_id="gini_country_dropdown",
                   component_property="value"))
def plot_gini_country_barchart(country):
    if not country:
        raise PreventUpdate
    df=gini_df[gini_df["Country Name"]==country].dropna(subset=[gini])
    fig=px.bar(df,
               x="year",
               y=gini,
               title=" - ".join([gini,country]))
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)