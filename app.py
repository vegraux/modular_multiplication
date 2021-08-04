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

from apps import circle, triangle

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True
)
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Circle", href="circle", active=True)),
        dbc.NavItem(dbc.NavLink("Triangle", href="triangle")),
    ],
    brand="Modular multiplication",
    brand_href="#",
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


if __name__ == "__main__":
    app.run_server(debug=True)
