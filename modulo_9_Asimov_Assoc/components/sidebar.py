import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd

from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app


## Layout
layout = dbc.Container([
    modal_novo_processo.layout, 
    modal_novo_advogado.layout, 
    modal_advogados.layout,
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("ASIMOV", style={'color':'yellow'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("ASSOCIATES", style={'color':'white'})
            ])
        ])
    ], style={'padding-top':'50px', 'margin-bottom':'100px'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(
                    dbc.NavLink([
                        html.I(className='fa fa-home dbc'), 
                        "\tINÍCIO"
                    ], href="/home", active=True, style={'text-align': 'left'})
                ),
                html.Br(),
                dbc.NavItem(
                    dbc.NavLink([
                        html.I(className='fa fa-plus-circle dbc'), 
                        "\tPROCESSOS"
                    ], id="processo_button", active=True, style={'text-align': 'left', 'cursor': 'pointer'})
                ),
                html.Br(),
                dbc.NavItem(
                    dbc.NavLink([
                        html.I(className='fa fa-user-plus dbc'), 
                        "\tADVOGADOS"
                    ], id="advogados_button", active=True, style={'text-align': 'left', 'cursor': 'pointer'})
                ),
            ], vertical= "lg", pills=True, fill=True) ## pills -> permite preencher o máximo de entorno que conseguir
        ])
    ])
], style={'height': '100vh', 'padding': '0px', 'position':'sticky', 'top': 0, 'backgroundColor': '#232423'})


## Callbacks
### Abrir modal Novo Advogado
@app.callback(
    Output('modal_novo_adv', "is_open"),
    Input('novo_adv_button', 'n_clicks'),
    Input("cancel_button_novo_adv", 'n_clicks'),
    State('modal_novo_adv', "is_open")
)
def toggle_modal(n, n2, is_open):
    if n or n2:
        return not is_open
    return is_open
### Abrir modal Advogados
@app.callback(
    Output('modal_advogados', "is_open"),
    Input('advogados_button', 'n_clicks'),
    Input('sair_button', 'n_clicks'),
    Input('novo_adv_button', 'n_clicks'),
    State('modal_advogados', "is_open")
)
def toggle_modal(n, n2, n3, is_open):
    if n or n2 or n3:
        return not is_open
    return is_open