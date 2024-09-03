import pandas as pd

def merge_concat_join():
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                       index=[0, 1, 2, 3])

    df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                       index=[4, 5, 6, 7])
    df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                       index=[8, 9, 10, 11])

    print(df1)
    print(df2)
    print(df3)

    #Concatenação

    pd_concat_vert = pd.concat([df1, df2, df3])
    pd_concat_horizontal = pd.concat([df1,df2,df3], axis=1)

    print('Concatenado Vertical: ')
    print(pd_concat_vert)
    #Vai expandir horizontalmente (usando NaNs)para criar uma matriz que encaixe todos os dfs
    print('Concatenado Horizontal: ')
    print(pd_concat_horizontal)

    #Merge -> permite mesclar matrizes por meio de uma coluna chave (tipo o join do SQL)

    esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})

    direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']})

    esq_dir_merged = pd.merge(esquerda, direita, how='inner', on='key')

    print("Merge: ")
    print(esq_dir_merged)

    esquerda_2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})

    direita_2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                            'key2': ['K0', 'K0', 'K0', 'K0'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']})

    esq_dir_merged_2 = pd.merge(esquerda_2, direita_2, on=['key1', 'key2'])
    esq_dir_merged_3 = pd.merge(esquerda_2, direita_2, how='outer', on=['key1', 'key2'])
    esq_dir_merged_4 = pd.merge(esquerda_2, direita_2, how='right', on=['key1', 'key2'])
    esq_dir_merged_5 = pd.merge(esquerda_2, direita_2, how='left', on=['key1', 'key2'])

    print('Merge com mais de uma chave (inner, outer, right, left)')
    print(esq_dir_merged_2)
    print(esq_dir_merged_3)
    print(esq_dir_merged_4)
    print(esq_dir_merged_5)

    #Join -> Tipo o merge mas focando em operações com os índices

    esquerda_join = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                             'B': ['B0', 'B1', 'B2']},
                            index=['K0', 'K1', 'K2'])

    direita_join = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                            'D': ['D0', 'D2', 'D3']},
                           index=['K0', 'K2', 'K3'])

    esq_join = esquerda_join.join(direita_join)
    esq_join_left = esquerda_join.join(direita_join, how="left")
    esq_join_inner = esquerda_join.join(direita_join, how="inner")
    esq_join_right = esquerda_join.join(direita_join, how="right")
    esq_join_outer = esquerda_join.join(direita_join, how="outer")

    print("Join (left/default,left, inner, right, outer): ")
    print(esq_join)
    print(esq_join_left)
    print(esq_join_inner)
    print(esq_join_right)
    print(esq_join_outer)


merge_concat_join()