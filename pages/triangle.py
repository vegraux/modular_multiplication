# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from pages.utils import make_triangle_figure

triangle_card_stride = [
    dbc.CardBody(
        [
            html.H5("Select stride of connecting node", className="card-title"),
            dcc.Slider(
                id="triangle-factor-slider",
                min=1,
                max=100,
                step=1,
                value=5,
                marks={k: str(k) for k in range(0, 101, 10)},
            ),
        ]
    )
]
triangle_card_num_points = [
    dbc.CardBody(
        [
            html.H5("Select number of points on each side of the triangle", className="card-title"),
            dcc.Slider(
                id="triangle-num-points-slider",
                min=3,
                max=100,
                step=1,
                value=30,
                marks={k: str(k) for k in range(0, 101, 10)},
            ),
        ]
    )
]
layout = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dbc.Card(triangle_card_stride, color="light", inverse=False)),
                dbc.Col(dbc.Card(triangle_card_num_points, color="light", inverse=False)),
            ]
        ),
        dbc.Row([dbc.Col(dcc.Graph(id="triangle-fig", figure=make_triangle_figure(30, 5)))]),
    ]
)
