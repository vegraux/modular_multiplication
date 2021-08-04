# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from pages.utils import make_circle_figure

N = 200
FACTOR = 2

circle_card_num_points = [
    dbc.CardBody(
        [
            html.H5("Select number of points on the circle", className="card-title"),
            html.P(
                "The number of uniformly spaced points on the circle boundary",
                className="card-text",
            ),
            dcc.Slider(
                id="circle-num-points-slider",
                min=10,
                max=400,
                step=30,
                value=200,
                marks={k: str(k) for k in range(100, 401, 100)},
            ),
        ]
    )
]
circle_card_factor = [
    dbc.CardBody(
        [
            html.H5("Select factor of multiplication", className="card-title"),
            html.P("The figure will change when the factor is changed", className="card-text"),
            dcc.Slider(
                id="circle-factor-slider",
                min=2,
                max=200,
                step=0.1,
                value=2,
                marks={k: str(k) for k in range(10, 201, 20)},
            ),
        ]
    )
]
layout = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dbc.Card(circle_card_factor, color="light", inverse=False)),
                dbc.Col(dbc.Card(circle_card_num_points, color="light", inverse=False)),
            ]
        ),
        dbc.Row(
            [dbc.Col(dcc.Graph(id="circle-fig", figure=make_circle_figure(N=N, factor=FACTOR)))]
        ),
    ]
)
