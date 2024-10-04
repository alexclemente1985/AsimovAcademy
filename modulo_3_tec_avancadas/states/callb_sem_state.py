import os
from pathlib import Path
import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

def callb_sem_state():
    app = dash.Dash(__name__)

    app.layout = html.Div(
        children=[
            dcc.Input(id="input-1", type="text", value="Montréal"),
            dcc.Input(id="input-2", type="text", value="Canada"),
            html.Div(id="number-output"),
        ]
    )

    @app.callback(
            Output("number-output", "children"),
            [
                Input("input-1", "value"),
                Input("input-2", "value")
            ]
    )
    def update_output(input1,input2):
        return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)

    app.run_server(debug=True, port=8052)

callb_sem_state()