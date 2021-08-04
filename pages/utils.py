# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

from typing import List

import numpy as np
import plotly.graph_objects as go
import seaborn as sns


def array_to_rgb(array: List) -> str:
    rgb_string = "rgb("
    for value in array:
        rgb_string += str(int(value * 255)) + ","
    return rgb_string[:-1] + ")"


def get_colors(N: int) -> List[str]:
    sns_colors = sns.cubehelix_palette(N, start=1, rot=3, dark=0.1, light=0.7)
    marker_colors = [array_to_rgb(color) for color in sns_colors]
    return marker_colors


def update_layout(fig: go.Figure):
    fig.update_layout(
        xaxis=dict(range=(-1.03, 1.03), zeroline=False),
        yaxis=dict(range=(-1.03, 1.03), zeroline=False),
        height=900,
        width=900,
        template="plotly_white",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        showlegend=False,
    )
    fig.update_xaxes(tickvals=[])
    fig.update_yaxes(tickvals=[])


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


def x_side1(t: int, points: int) -> float:
    return 1 - 1 / points * t


def y_side1(t: int, points: int) -> float:
    return -1 + 2 * t / points


def x_side2(t: int, points: int) -> float:
    return -1 / points * t


def y_side2(t: int, points: int) -> float:
    return 1 - 2 / points * t


def x_side3(t: int, points: int) -> float:
    return -1 + 2 / points * t


def y_side3() -> float:
    return -1


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
