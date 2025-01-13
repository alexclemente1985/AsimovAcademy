from pathlib import Path
import pandas as pd
import streamlit as st
from datetime import datetime

def adicionando_linhas_streamlit():
    pasta_datasets = Path.joinpath(Path(__file__).parents[3], 'datasets')

    caminho_vendas = Path.joinpath(pasta_datasets, 'vendas.csv')
    caminho_filiais = Path.joinpath(pasta_datasets, 'filiais.csv')
    caminho_produtos = Path.joinpath(pasta_datasets, 'produtos.csv')

    df_vendas = pd.read_csv(caminho_vendas, decimal=',', sep=';', index_col=0)
    df_filiais = pd.read_csv(caminho_filiais, decimal=',', sep=';', index_col=0)
    df_produtos = pd.read_csv(caminho_produtos, decimal=',', sep=';', index_col=0)

    df_filiais['cidade/estado'] = df_filiais['cidade']+'/'+df_filiais['estado']
    lista_filiais = df_filiais['cidade/estado'].to_list()
    filial_selecionada = st.sidebar.selectbox('Selecione a filial:', lista_filiais)

    #Conversão da Serie uma lista de string (.iloc[0]), que vai ser convertida para lista a partir dos valores da string (pq os vendedores estão dentro de uma "lista" nas células da tabela de filiais)
    lista_vendedores = df_filiais.loc[df_filiais['cidade/estado'] == filial_selecionada, 'vendedores'].iloc[0]
    lista_vendedores = lista_vendedores.strip('][').replace("'", '').split(', ')
    vendedor_selecionado = st.sidebar.selectbox('Selecione o vendedor:',
                                            lista_vendedores)

    lista_produtos = df_produtos['nome'].to_list()
    produto_selecionado = st.sidebar.selectbox('Selecione o produto:',
                                            lista_produtos)

    nome_cliente = st.sidebar.text_input('Nome do cliente')

    genero_selecionado = st.sidebar.selectbox('Genêro do cliente:',
                                            ['masculino', 'feminino'])

    forma_pag_selecionado = st.sidebar.selectbox('Forma de pagamento',
                                                ['credito', 'pix', 'boleto'])


    if st.sidebar.button('Adicionar nova venda'):
        lista_adicionar = [df_vendas['id_venda'].max() + 1,
                       filial_selecionada,
                       vendedor_selecionado,
                       produto_selecionado,
                       nome_cliente,
                       genero_selecionado,
                       forma_pag_selecionado]
        df_vendas.loc[datetime.now()] = lista_adicionar
        df_vendas.to_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';')
        st.success('Venda adicionada')

    st.dataframe(df_vendas, height=800)



adicionando_linhas_streamlit()