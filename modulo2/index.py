from pathlib import Path

import pandas as pd
from numpy.random import randn


def index():
    df = pd.DataFrame(randn(5, 4), index=["A", "B", "C", "D", "E"], columns="W Y X Z".split())
    print(df.index)
    print(df.columns)
    df_index_reset = df.reset_index()
    print(df_index_reset)
    df.reset_index(inplace=True)
    print(df)
    df.set_index("index", inplace=True)
    print(df)

    novoindex = 'CA NY WY OR CO'.split()
    df['novo_index'] = novoindex
    print(df)
    # Salvando índices em uma coluna nova (guardando histórico e resetando)
    df.reset_index(inplace=True)
    # Setando novos índices (se não fizer passo anterior, apaga os antigos)
    df.set_index('novo_index', inplace=True)
    print(df)
    print(df.index)

    # Níveis de índice
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2', ]
    inside = [1, 2, 3, 1, 2, 3]

    # zip -> encaixa as duas listas e cria uma lista de tuplas com as combinações
    hier_index = list(zip(outside, inside))
    print(hier_index)

    # Usando pandas para dispor da lista de tuplas acima como índices
    hier_index = pd.MultiIndex.from_tuples(hier_index)
    print(hier_index)

    # Agrupamento de valores em índices (ideal para estudos de depts agrupados por filiais, por ex.)
    ## Índices multinível
    df = pd.DataFrame(randn(6, 2), index=hier_index, columns=['A', 'B'])
    print(df)
    # Cria uma matriz 6x2 com elementos aleatórios
    print(randn(6, 2))

    # Obtenção da primeira linha do dataframe anterior, indexado pelas colunas
    print(df.loc["G1"].loc[1])

    # Criando rótulos para colunas de índices
    df.index.names = ['Grupo', 'Número']
    print(df)

    # Pega todas as linhas, indexadas por "Grupo", que estiverem com o subnível "Número" = 2
    print(df.xs(2, level="Número"))
    # Pega todos os registros do índice "G2"
    print(df.xs('G2'))
    # Pega todos os registros com índice "Número" = 3 (como é inteiro, deve-se indicar o level)
    print(df.xs(3, level=1))
    # Pega todas as linhas, indexadas por "Grupo", que estiverem com o subnível "Número" = 3 e grupo = "G1"
    print(df.xs(('G1', 3), level=[0, "Número"]))


index()
