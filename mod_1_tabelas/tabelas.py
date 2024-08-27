from pathlib import Path

import pandas as pd


def tabelas():
    data = [1, 2, 3, 4]
    # Criando tabela matriz
    data_2 = [[1, 2], [3, 4], [5, 6]]
    # Criando tabela com colunas nomeadas (uso de dicionário)
    data_3 = {'Nome': ['Alexandre', 'Jonas', 'Caio', 'Priscilla'],
              'Sobrenome': ['Clemente', 'de Sá', 'Alexandre', 'Souza']}
    # Criando tabela com lista de dicionários
    data_4 = [{'Nome': 'Joel', 'Sobrenome': 'Pinheiro'},
              {'Nome': 'Nanci', 'Sobrenome': 'Clemente'},
              {'Nome': 'Claudia', 'Sobrenome': 'Regina'},
              {'Nome': 'Nilton', 'Sobrenome': 'Pereira'}, ]

    df = pd.DataFrame(data)
    df_2 = pd.DataFrame(data_2)
    # Criando dataframe com index customizado
    df_3 = pd.DataFrame(data_3, index=['pessoa', 'pessoa2', 'pessoa3', 'pessoa4'])
    df_4 = pd.DataFrame(data_4)

    print(df)
    print(df_2)
    print(df_3)
    print(df_4)

    #Retornando colunas
    print(df_3.columns)
    #Retornando os index
    print(df_3.index)
    #Retornando a forma (shape)
    print(df_3.shape, '\nNúmero de linhas: ', df_3.shape[0], '\nNúmero de colunas: ', df_3.shape[1])

    # Importando dados de tabelas
    datasets = Path.joinpath(Path.cwd().parent,'datasets')
    print(datasets)
    #Criando tabela sobre xlsx (a partir da aba 'Sheet1' e usando indice a coluna 1)
    ## decimal -> para evitar problemas com dados com virgula (padrão brasileiro) ou ponto (padrão americano)
    ## usecols -> para carregar apenas as colunas informadas na lista
    tabela_vendas = pd.read_excel(datasets/'vendas.xlsx',
                                  sheet_name='Sheet1',
                                  index_col=1,
                                  decimal=',',
                                  usecols=['id_venda','data','filial'])

    # Carregando tabela .csv (importante indicar o tipo de separador 'sep')
    tabela_vendas_2 = pd.read_csv(datasets / 'vendas.csv',
                                  index_col=1,
                                  decimal=',',
                                  usecols=['id_venda', 'data', 'filial'],
                                  sep=';')

    print(tabela_vendas)
    print(tabela_vendas_2)
tabelas()
