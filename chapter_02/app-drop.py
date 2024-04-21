import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output,Input

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    dcc.Dropdown(id="color-dropdown",
                 options=[{"label":color,
                           "value":color}
                           for color in ["blue","green","yellow"]
                           ]),
    html.Br(),
    html.Div(id="color-output")
])

@app.callback(Output(component_id="color-output",
                     component_property="children"),
              Input(component_id="color-dropdown",
                    component_property="value"))
def display_selected_color(color):
    if color is None:
        color = "nothing"
    return "you selected "+ color

if __name__=="__main__":
    app.run_server(debug=True)