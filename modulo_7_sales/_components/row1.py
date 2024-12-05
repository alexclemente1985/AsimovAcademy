from app import *
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from assets.styles import *
from dataset import *


row1 = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Legend("Sales Analytics")
                    ], sm=8),
                    dbc.Col([
                        html.I(className='fa fa-balance-scale', style={'font-size':'300%'})
                    ], sm=4, align="center")
                ]),
                dbc.Row([
                    dbc.Col([
                        ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                        html.Legend('Asimov Academy - Alex Version')
                    ])
                ], style={'margin-top': '10px'}),
                dbc.Row([
                    dbc.Button('Visite o Site', href="https://asimov.academy", target='_blank')
                ], style={'margin-top':'10px'})
            ])
        ], style=tab_card)
    ], sm=4, lg=2),
    dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend('Top Consultores por Equipe')
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph1', className='dbc', config=config_graph)
                        ], sm=12, md=7),
                        dbc.Col([
                            dcc.Graph(id='graph2', className='dbc', config=config_graph)
                        ], sm=12, lg=5)
                    ])
                ])
            ], style=tab_card)
        ], sm=12, lg=7),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col([
                            html.H5('Escolha o Mês'),
                            dbc.RadioItems(
                                id="radio-month",
                                options=options_month,
                                value=0,
                                inline=True,
                                labelCheckedClassName="text-success",
                                inputCheckedClassName="border border-success bg-success",
                            ),
                            html.Div(id='month-select', style={'text-align': 'center', 'margin-top': '30px'}, className='dbc')
                        ])
                    )
                ])
            ], style=tab_card)
        ], sm=12, lg=3)
    ], className='g-2 my-auto', style={'margin-top': '7px'})
