# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import circle, triangle
from pages.utils import make_circle_figure, make_triangle_figure

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True
)
server = app.server
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Circle", href="circle", style={"fontSize": 25})),
        dbc.NavItem(dbc.NavLink("Triangle", href="triangle", style={"fontSize": 25})),
    ],
    brand="Modular multiplication",
    brand_style={"fontSize": 40},
    brand_href="/",
    color="primary",
    dark=True,
)

layout = html.Div([dcc.Location(id="url", refresh=False), navbar, html.Div(id="page-content")])

app.layout = dbc.Container(layout)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if (pathname == "/circle") or (pathname == "/"):
        return circle.layout
    elif pathname == "/triangle":
        return triangle.layout
    else:
        return "404"


@app.callback(
    Output("circle-fig", "figure"),
    [Input("circle-num-points-slider", "value"), Input("circle-factor-slider", "value")],
)
def update_circle_data(N, factor):
    return make_circle_figure(N=N, factor=factor)


@app.callback(
    Output("triangle-fig", "figure"),
    [Input("triangle-num-points-slider", "value"), Input("triangle-factor-slider", "value")],
)
def update_triangle_data(num_points, stride):
    return make_triangle_figure(points_per_side=num_points, stride=stride)


if __name__ == "__main__":
    app.run_server(debug=True)
