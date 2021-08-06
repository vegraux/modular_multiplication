# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

from typing import List

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
