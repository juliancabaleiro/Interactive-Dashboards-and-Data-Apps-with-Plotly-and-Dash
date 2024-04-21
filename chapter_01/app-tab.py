import dash
from dash import html
import dash_bootstrap_components as dbc

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    dbc.Row([
        dbc.Col(html.Div("Colum 1")),
        dbc.Col(html.Div("Colum 2"),
                        lg={"size":1,
                          "offset":5}),
        dbc.Col(html.Div("Col 3"),
                lg={"size":1,
                    "offset":2})
    ]),
    dbc.Row([
        dbc.Col(html.Div("Colum 4")),
        dbc.Col(html.Div("Colum 5")),
        dbc.Col(html.Div("Col 6"))
    ]),
    dbc.Tabs([
        dbc.Tab([
            html.Ul(["HOla"])
        ], label="primera"),
        dbc.Tab([
            html.Ul(["HOla2"])
        ], label="segunda")
    ]),
    html.H1("Titulo")
])

if __name__=="__main__":
    app.run_server(debug=True)