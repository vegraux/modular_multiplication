# -*- coding: utf-8 -*-

"""

"""

__author__ = "Vegard Ulriksen Solberg"
__email__ = "vegardsolberg@hotmail.com"

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_defer_js_import as dji
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import circle, info, square, triangle
from pages.circle import make_circle_figure
from pages.square import make_square_figure
from pages.triangle import make_triangle_figure

external_scripts = [
    "https://code.jquery.com/jquery-3.2.1.slim.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
    "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js",
]

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    external_scripts=external_scripts,
)

mathjax_script = dji.Import(
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG"
)
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                tex2jax: {
                inlineMath: [ ['$','$'],],
                processEscapes: true
                }
            });
            </script>
            {%renderer%}
        </footer>
    </body>
</html>
"""
server = app.server
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Circle", href="circle", style={"fontSize": 25})),
        dbc.NavItem(dbc.NavLink("Triangle", href="triangle", style={"fontSize": 25})),
        dbc.NavItem(dbc.NavLink("Square", href="square", style={"fontSize": 25})),
        dbc.NavItem(dbc.NavLink("Info", href="info", style={"fontSize": 25})),
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

    elif pathname == "/square":
        return square.layout

    elif pathname == "/info":
        return info.layout

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


@app.callback(
    Output("square-fig", "figure"),
    [Input("square-num-points-slider", "value"), Input("square-factor-slider", "value")],
)
def update_square_data(num_points, stride):
    return make_square_figure(points_per_side=num_points, stride=stride)


if __name__ == "__main__":
    app.run_server(debug=True)
