import dash
from dash import html, dcc, Output, Input, dash_table
import dash_bootstrap_components as dbc
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def visualizando_tabela():
    app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

    pasta_datasets = Path.joinpath(Path(__file__).parents[2], 'datasets')
    caminho_vendas = Path.joinpath(pasta_datasets, 'vendas.csv')
    df_vendas = pd.read_csv(caminho_vendas, sep=';')

    colunas = [{"name": i, "id": i} for i in df_vendas.columns]


    #Dificuldade para alterar estilo
    table = html.Div(
        children=[
            dbc.Table.from_dataframe(df_vendas,
                                     bordered=True,
                                     dark=True,
                                     hover=True,
                                     responsive=True,
                                     striped=True,
                                     color='dark',
                                     id='sales-table'
                                     ),
        ]
    )

    #Melhor para alterar estilo
    table2 = html.Div(
        [
            dash_table.DataTable(
                id='sales-table',
                #Necessário passar o nome das colunas
                columns=colunas,
                #'records' permite a ligação coluna->valor na tabela
                data = df_vendas.to_dict('records'),
                #Habilitando filtro nativo da tabela
                filter_action='native',
                #Estilização da tabela
                style_cell={'padding': '5px', 'textAlign': 'right', 'background':'grey'},
                style_header={
                    'backgroundColor': 'grey',
                    'fontWeight': 'bold',
                    'color': 'white'
                },
                #Estilização para 'zebrar' a lista
                style_data={
                    'color': '#363636',
                    'backgroundColor': 'white'
                },
                style_data_conditional=[{
                    'if':{'row_index':'odd'},
                    'backgroundColor':'	#363636',
                    'color': 'white'
                }],
                #Estilização condicional
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'data'},
                        'textAlign': 'left'
                    }
                ]
            )
        ]
    )


    app.layout = dbc.Container(
        children=[
            dbc.Row([
                html.H1('Tabela vendas'),
                table2
            ])
        ]
    )



    app.run_server(debug=True, port=8051)



if __name__ == "__main__":
    visualizando_tabela()
