import os
from pathlib import Path
import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State

def callb_com_state():
    app = dash.Dash(__name__)

    app.layout = html.Div(
        children=[
            dcc.Input(id="input-1", type="text", value="Montréal"),
            dcc.Input(id="input-2", type="text", value="Canada"),
            html.Button(id="submit-button", n_clicks=0, children="Enviar"),
            html.Div(id="output-state"),
        ]
    )
    #State -> guarda os valores no estado, e só mostra se houver variação de Input
    @app.callback(
            Output("output-state", "children"),
            [Input("submit-button", "n_clicks")],
            [
                State("input-1", "value"),
                State("input-2", "value"),
            ]
    )
    def update_output(n_clicks,input1,input2):
        return u'''Input 1 is "{}" and Input 2 is "{}".
        The Button has been pressed {} times'''.format(input1, input2, n_clicks)

    app.run_server(debug=True, port=8052)

callb_com_state()