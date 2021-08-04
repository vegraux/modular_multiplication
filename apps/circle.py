# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps.utils import card_factor, card_num_points, make_circle_figure

N = 200
FACTOR = 2


layout = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_factor, color="light", inverse=False)),
                dbc.Col(dbc.Card(card_num_points, color="light", inverse=False)),
            ]
        ),
        dbc.Row(
            [dbc.Col(dcc.Graph(id="circle-fig", figure=make_circle_figure(N=N, factor=FACTOR)))]
        ),
    ]
)


@app.callback(
    Output("circle-fig", "figure"),
    [Input("circle-num-points-slider", "value"), Input("circle-factor-slider", "value")],
)
def update_data(N, factor):
    return make_circle_figure(N=N, factor=factor)
