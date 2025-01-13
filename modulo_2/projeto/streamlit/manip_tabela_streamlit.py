from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def manip_tabela_streamlit():
    pasta_datasets = Path.joinpath(Path(__file__).parents[3], 'datasets')
    caminho_vendas = Path.joinpath(pasta_datasets, 'vendas.csv')
    df_vendas = pd.read_csv(caminho_vendas, decimal=',', sep=';', index_col=0)

    colunas = list(df_vendas.columns)
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas, colunas) #placeholder, opções e valores do select múltiplo (começa com tudo escolhido)

    col1, col2 = st.sidebar.columns(2)

    col_filtro = col1.selectbox('Selecione a coluna', [c for c in colunas if c not in ['id_venda']])
    valor_filtro = col2.selectbox('Selecione o valor', list(df_vendas[col_filtro].unique()))

    status_filtrar = col1.button('Filtrar')
    status_limpar = col2.button('Limpar')

    if status_filtrar:
        st.dataframe(df_vendas.loc[df_vendas[col_filtro] == valor_filtro, colunas_selecionadas], height=800)
    elif status_limpar:
        st.dataframe(df_vendas[colunas_selecionadas], height=800)
    else:
        st.dataframe(df_vendas[colunas_selecionadas], height=800)

manip_tabela_streamlit()