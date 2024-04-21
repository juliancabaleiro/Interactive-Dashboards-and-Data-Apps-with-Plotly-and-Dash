import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pandas as pd

poverty_data=pd.read_csv(filepath_or_buffer="data\PovStatsData.csv")
regions = ['East Asia & Pacific', 'Europe & Central Asia', 'Fragile and conflict affected situations', 'High income',
'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income', 'Low income',
'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia','Sub-Saharan Africa', 'Upper middle income', 'World'] 
population_df=poverty_data[~poverty_data["Country Name"].isin(regions) & (poverty_data["Indicator Name"]=="Population, total")]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    html.H1("Poverty and Equity Database"),
    html.Br(),
    html.H2("The world bank"),
    html.Br(),
    dcc.Dropdown(id="country",
                 options=[{"label":country,
                          "value":country}
                          for country in poverty_data["Country Name"].unique()]),
    html.Div(id="report"),
    html.Br(),
    dcc.Dropdown(id="year_dropdown",
                 value="2010",
                 options=[{"label": year,
                           "value": str(year)}
                           for year in range(1974,2019)]),
    dcc.Graph(id="population_chart"),
    html.Br(),
    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li("Number of Economies: 170"),
                html.Li("Temporal Coverge: 1974-2019"),
                html.Li("Update Frecuency: Quarterly"),
                html.Li(["Sourcer: ",
                         html.A("https://datacatalog.worldbank.org/dataset/poverty-and-equity-database",
                                href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database"
                                )
                        ])
                    ])
                ],label="Key Facts"),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li("Book title: Interactive Dashboards and Data Apps with Plotly and Dash"),
                html.Li(["github repo: ",
                         html.A("https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash",
                                href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash")
                                ])
                    ])
                ],label="project Info")
            ])      
])

@app.callback(Output(component_id="population_chart",
                     component_property="figure"),
              Input(component_id="year_dropdown",
                    component_property="value"))
def plot_countries_by_population(year, pop_df=population_df):
    year_df=pop_df[["Country Name",year]].sort_values(year,ascending=False)[:20]
    fig=go.Figure()
    fig.add_bar(x=year_df["Country Name"],y=year_df[year])
    fig.layout.title=f"Top twenty countries by population - {year}"
    return fig

@app.callback(Output(component_id="report",
                     component_property="children"),
              Input(component_id="country",
                    component_property="value"))
def display_country_report(country,pov_data=poverty_data):
    if country is None:
        return ""
    filtered_df=pov_data[(pov_data["Country Name"]==country)&
                        (pov_data["Indicator Name"]=="Population, total")]
    population=filtered_df.loc[:,"2010"].values[0]
    return [html.H3(country),
            f"The population of {country} in 2010 was {population:,.0f}."]
    
if __name__=="__main__":
    app.run_server(debug=True)