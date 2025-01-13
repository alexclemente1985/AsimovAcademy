import dash
from dash import html,dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

from app import *
from components import home, sidebar

### Layout
app.layout = dbc.Container([
    #### Store e location
    dcc.Location(id="url"),
    dcc.Store(id='store_intermediario', data={}),
    dcc.Store(id='store_adv', data={}),
    dcc.Store(id='store_proc',data={}),
    html.Div(id='div_fantasma'),

    #### Layout
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '8px'}),
        dbc.Col([
            dbc.Container(
                id='page-content', 
                fluid= True, 
                style={'height':'100%', 'width': '100%', 'paddingLeft':'14px'}
            )
        ], md=10, style={'padding': '0px'})
    ])
], fluid = True)

### Callbacks

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page(pathname):
    if pathname == '/home' or pathname =='/':
        return home.layout
    else:
        return dbc.Container([
            html.H1('404: Not Found', className="text-danger"),
            html.Hr(),
            html.P(f"O caminho '{pathname}' não foi reconhecido..."),
            html.P("Use a NavBar para retornar ao sistema de maneira correta.")
        ])

@app.callback(
    Output('div_fantasma','children'),
    Input('store_adv','data'),
    Input('store_proc', 'data')
)
def update_file(adv_data, proc_data):
    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
