import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app

from _components.component1 import *

def index():
        app.layout = dbc.Container(
            children=[
                component1
            ], fluid=True
        )

        app.run_server(debug=True)


index()