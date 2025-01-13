from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def visualizando_tabela_str():
    app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

    pasta_datasets = Path.joinpath(Path(__file__).parents[2], 'datasets')
    caminho_vendas = Path.joinpath(pasta_datasets, 'vendas.csv')
    df_vendas = pd.read_csv(caminho_vendas, sep=';')

    #colunas = [{"name": i, "id": i} for i in df_vendas.columns]

    st.dataframe(df_vendas)

visualizando_tabela_str()