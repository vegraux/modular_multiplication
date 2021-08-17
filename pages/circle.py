# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from plotly import graph_objects as go

from pages.utils import get_colors, update_layout

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


def make_circle_figure(N: int = 150, factor: int = 2) -> go.Figure:
    fig = go.Figure()
    fig.add_shape(type="circle", x0=-1, y0=-1, x1=1, y1=1, line_color="black", layer="below")
    update_layout(fig)
    angles = np.linspace(0, 2 * np.pi, N + 1)
    angles_multiplied = (angles * factor) % (2 * np.pi)
    x, y = np.cos(angles[:-1]), np.sin(angles[:-1])
    x_multiplied, y_multiplied = (np.cos(angles_multiplied[:-1]), np.sin(angles_multiplied[:-1]))
    marker_colors = get_colors(N)
    for i in range(N):
        fig.add_trace(
            go.Scattergl(
                x=[x[i], x_multiplied[i]],
                y=[y[i], y_multiplied[i]],
                mode="lines",
                marker={"color": marker_colors[i]},
                line=dict(width=1),
            )
        )
    title = f"<b>Multiplying by {factor} on a circle with {N} points</b>"
    fig.update_layout(title=title)
    return fig


def circle_example_figure():
    N = 10
    factor = 2
    fig = make_circle_figure(N, factor)
    for i in range(10):
        angle = i * 2 * np.pi / N
        x, y = np.cos(angle), np.sin(angle)
        fig.add_annotation(x=x * 1.05, y=y * 1.05, text=i, showarrow=False, font=dict(size=16))
    fig.update_layout(
        height=730,
        width=730,
        xaxis=dict(range=(-1.06, 1.06), zeroline=False),
        yaxis=dict(range=(-1.06, 1.06), zeroline=False),
    )
    return fig


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
