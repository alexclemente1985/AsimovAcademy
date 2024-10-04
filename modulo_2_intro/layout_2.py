import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc

def layout_dash_2():
    app = dash.Dash(__name__)

    app.layout = html.Div(
        children=[
            html.Label("Dropdown de estados brasileiros"),
            dcc.Dropdown(
                id="dp-1",
                options=[
                        {"label":"Rio Grande do Sul", "value": "RS"},
                        {"label":"Rio de Janeiro", "value": "RJ"},
                        {"label":"São Paulo", "value": "SP"},
                    ],
                value="RS",
                style={"margin-bottom":"50px"}
                ),
            html.Label("Checklist de estados brasileiros"),
            dcc.Checklist(
                id="cl-1",
                options=[
                        {"label":"Rio Grande do Sul", "value": "RS"},
                        {"label":"Rio de Janeiro", "value": "RJ"},
                        {"label":"São Paulo", "value": "SP"},
                    ],
                value=["RS","RJ","SP"],
                style={"margin-bottom":"50px"}
                ),
            html.Label("Text Input"),
            dcc.Input(
                id="in-1",
                value="SP",
                type="text",
                style={"margin-bottom":"50px"}
            ),
            html.Label("Slider"),
            dcc.Slider(
                id="sl-1",
                min=0,
                max=9,
                marks={i: f"Label {i}" if i == 1 else str(i) for i in range(1,6) },
                value=5
            )

            ]
        )

    app.run_server(debug=True, port=8053)

layout_dash_2()