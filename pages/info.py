import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_defer_js_import as dji
import dash_html_components as html

from pages.circle import circle_example_figure

square_info_card = [
    dbc.CardBody(
        [
            html.H5("Select stride of connecting node", className="card-title"),
            html.P(
                "The number of uniformly spaced points on the circle boundary",
                className="card-text",
            ),
        ]
    )
]

circle_text = r"""The circle figure is made by first partitioning the boundary into $N$ equally
spaced points. Because the points on the circle are uniformly partitioned, each integer $i$ can be
expressed by an angle  $\delta = \frac{2\pi}{N} i$. Imagine wrapping the real number line around
the circle with period $N$ such that $0, N, 2N, \dots$ land on the point corresponding to $0^{o}$.
Every integer is connected by a chord to another point on the circle boundary, based on the
chosen factor of multiplication $c$. The corresponding end-point for the chord of an integer is
therefore $(\cos c \delta, \sin c \delta)$, where $c$ is the factor of multiplication. This figure
can therefore be interpreted as a modular visual representation of multiplication
"""
circle_example = r"""Consider the following example where $N=10$ and $c=2$. 0 connects to 0, 1 to
2, 2 to 4 etc. But where does 6 land ($6*2=12$) when we only have 10 points? Because we imagine
wrapping the number line around the circle, 12 is the same as 2 (12 mod 10 = 2). This examples is
rather visually uninteresting until we up the number of points on the circle.
"""

circle_info_card = [
    dbc.CardBody(
        [
            html.H3("Circle", className="card-title"),
            html.P(circle_text),
            html.H5("Example"),
            circle_example,
            html.Br(),
            html.Br(),
            html.Div(
                dcc.Graph(id="circle-example-fig", figure=circle_example_figure()),
                className="container",
                style={"maxWidth": "750px"},
            ),
        ]
    )
]

mathjax_script = dji.Import(
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG"
)
axis_latex_script = dji.Import(
    src="https://cdn.jsdelivr.net/gh/yueyericardo/simuc@master/apps/dash/resources/redraw.js"
)

layout = html.Div(
    [
        html.Br(),
        dbc.Card(circle_info_card, color="light", inverse=False),
        dbc.Card(square_info_card, color="light", inverse=False),
        dcc.Markdown("jeg er $N=3$", dangerously_allow_html=True),
        mathjax_script,
        axis_latex_script,
    ]
)
