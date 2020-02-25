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


def make_circle_figure(N=150, factor=2):
    fig = go.Figure()
    fig.add_shape(
        type="circle", x0=-1, y0=-1, x1=1, y1=1, line_color="black", layer="below"
    )

    fig.update_layout(
        xaxis=dict(range=(-1.1, 1.1), zeroline=False),
        yaxis=dict(range=(-1.1, 1.1), zeroline=False),
        height=800,
        width=800,
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

    ids = [factor * i % N for i in range(N)]
    for i in range(N):
        fig.add_trace(
            go.Scatter(
                x=x[[i, ids[i]]],
                y=y[[i, ids[i]]],
                mode="lines",
                marker_color="gray",
                line=dict(width=1),
            )
        )
    fig.update_layout(title=f"Multiplying by {factor} on a circle with {N} points")
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
