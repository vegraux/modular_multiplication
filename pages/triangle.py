# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objects as go

from pages.utils import get_colors, update_layout

triangle_card_stride = [
    dbc.CardBody(
        [
            html.H5("Select stride of connecting node", className="card-title"),
            dcc.Slider(
                id="triangle-factor-slider",
                min=0,
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


def y_side3() -> float:
    return -1


def x_side3(t: int, points: int) -> float:
    return -1 + 2 / points * t


def y_side2(t: int, points: int) -> float:
    return 1 - 2 / points * t


def x_side2(t: int, points: int) -> float:
    return -1 / points * t


def y_side1(t: int, points: int) -> float:
    return -1 + 2 * t / points


def x_side1(t: int, points: int) -> float:
    return 1 - 1 / points * t


def get_triangle_points(points: int) -> (list, list):
    x, y = [], []

    for point in range(points):
        x.append(x_side1(point, points))
        y.append(y_side1(point, points))

    for point in range(points):
        x.append(x_side2(point, points))
        y.append(y_side2(point, points))

    for point in range(points):
        x.append(x_side3(point, points))
        y.append(y_side3())

    return x, y


def make_triangle_figure(points_per_side: int, stride: int) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=[-1, 1, 0, -1], y=[-1, -1, 1, -1], mode="lines", line={"color": "gray"})
    )
    x, y = get_triangle_points(points_per_side)
    update_layout(fig)

    N = len(x)
    marker_colors = get_colors(N)
    for i in range(N):
        map_i = int(i + N / 3 + stride) % N
        fig.add_trace(
            go.Scattergl(
                x=[x[i], x[map_i]],
                y=[y[i], y[map_i]],
                mode="lines",
                line=dict(width=1),
                marker={"color": marker_colors[i]},
            )
        )
    title = (
        f"<b>Connecting nodes with stride {stride} on a triangle with"
        f" {points_per_side} points on each side</b>"
    )
    fig.update_layout(title=title)
    return fig


def triangle_example_figure():
    points_per_side = 3
    stride = 1
    fig = make_triangle_figure(points_per_side=points_per_side, stride=stride)
    xs, ys = get_triangle_points(points_per_side)

    for i, (x, y) in enumerate(zip(xs, ys)):
        fig.add_annotation(
            x=x * 1.08,
            y=y * 1.08,
            text=i % points_per_side,
            showarrow=False,
            font=dict(size=16),
            yshift=10,
        )
    fig.update_layout(
        height=730,
        width=730,
        xaxis=dict(range=(-1.1, 1.1), zeroline=False),
        yaxis=dict(range=(-1.1, 1.1), zeroline=False),
    )
    return fig


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
