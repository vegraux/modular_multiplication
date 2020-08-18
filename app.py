# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from src.utils import make_circle_figure, card_factor, card_max_count
from dash.dependencies import Input, Output

N = 200
FACTOR = 2

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
header = dbc.Jumbotron(
    [
        html.H1("Modular multiplication", className="display-3"),
        html.Hr(className="my-2"),
        html.P("Drag the sliders and see what happens!"),
    ]
)

layout = html.Div(
    [
        header,
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_factor, color="light", inverse=False)),
                dbc.Col(dbc.Card(card_max_count, color="light", inverse=False)),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="circle-fig", figure=make_circle_figure(N=N, factor=FACTOR)
                    )
                )
            ]
        ),
    ]
)

app.layout = dbc.Container(layout)


@app.callback(
    Output("circle-fig", "figure"),
    [Input("max-count-slider", "value"), Input("factor-slider", "value")],
)
def update_data(N, factor):
    return make_circle_figure(N=N, factor=factor)


if __name__ == "__main__":
    app.run_server(debug=True)
