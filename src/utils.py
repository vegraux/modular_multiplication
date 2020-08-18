# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns


def array_to_rgb(array):
    rgb_string = "rgb("
    for value in array:
        rgb_string += str(int(value * 255)) + ","
    return rgb_string[:-1] + ")"


def make_circle_figure(N=150, factor=2):
    fig = go.Figure()
    fig.add_shape(
        type="circle", x0=-1, y0=-1, x1=1, y1=1, line_color="black", layer="below"
    )

    fig.update_layout(
        xaxis=dict(range=(-1.1, 1.1), zeroline=False),
        yaxis=dict(range=(-1.1, 1.1), zeroline=False),
        height=1050,
        width=1050,
        template="plotly_white",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        showlegend=False,
    )
    fig.update_xaxes(tickvals=[])
    fig.update_yaxes(tickvals=[])
    angles = np.linspace(0, 2 * np.pi, N + 1)
    x = np.cos(angles[:-1])
    y = np.sin(angles[:-1])
    sns_colors = sns.cubehelix_palette(N, start=1, rot=3, dark=0.1, light=0.7)
    marker_colors = [array_to_rgb(color) for color in sns_colors]
    ids = [(factor * i) % N for i in range(N)]
    for i in range(N):
        fig.add_trace(
            go.Scattergl(
                x=x[[i, ids[i]]],
                y=y[[i, ids[i]]],
                mode="lines",
                marker_color=marker_colors[i],
                line=dict(width=1),
            )
        )
    title = f"<b>Multiplying by {factor} on a circle with {N} points</b>"
    fig.update_layout(title=title)
    return fig


card_factor = [
    dbc.CardBody(
        [
            html.H5("Select factor of multiplication", className="card-title"),
            html.P(
                "The figure will change when the factor is changed",
                className="card-text",
            ),
            dcc.Slider(
                id="factor-slider",
                min=2,
                max=200,
                step=1,
                value=2,
                marks={k: str(k) for k in range(10, 201, 20)},
            ),
        ]
    )
]

card_max_count = [
    dbc.CardBody(
        [
            html.H5("Select number of points on the circle", className="card-title"),
            html.P(
                "The number of uniformly spaced points on the circle boundary",
                className="card-text",
            ),
            dcc.Slider(
                id="max-count-slider",
                min=10,
                max=400,
                step=30,
                value=200,
                marks={k: str(k) for k in range(100, 401, 100)},
            ),
        ]
    )
]
