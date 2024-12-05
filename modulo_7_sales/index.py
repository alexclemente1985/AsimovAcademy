import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from app import app
from pathlib import Path
from _components.row1 import *
from assets.styles import *
from dataset import *


def index():
    server = app.server

    # ==== Layout ==== #

    app.layout = dbc.Container(children=[
        #html.H1('Teste carai')
        row1
    ], fluid=True, style={'height':'100vh'})

    # ==== Callbacks ==== #

    #Gráficos 1 e 2
    @app.callback(
        Output('graph1', 'figure'),
        Output('graph2', 'figure'),
        Output('month-select', 'children'),
        Input('radio-month', 'value'),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value")
    )
    def graph1(month, toggle):
        template = template_theme1 if toggle else template_theme2

        mask = month_filter(month)
        df_1 = df.loc[mask]

        df_1 = df_1.groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()
        df_1 = df_1.sort_values(ascending=False)
        df_1 = df_1.groupby('Equipe').head(1).reset_index()

        fig1 = go.Figure(go.Bar(x=df_1['Consultor'], y=df_1['Valor Pago'], textposition='auto', text=df_1['Valor Pago']))
        fig1.update_layout(main_config, height=200, template=template)
        fig2 = go.Figure(go.Pie(labels=df_1['Consultor'] + ' - ' + df_1['Equipe'], values=df_1['Valor Pago'], hole=.6))
        fig2.update_layout(main_config, height=200, template=template, showlegend=False)

        select = html.H1(convert_to_text(month))

        return fig1, fig2, select

    
    app.run_server(debug=True, port=8051)


index()