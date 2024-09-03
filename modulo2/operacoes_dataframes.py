import pandas as pd


def operacoes_dataframes():
    df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
    print(df.head())
    #verificação de consumo de memória com as colunas
    print(df.info())
    print(df.memory_usage())

    #retorna array com valores únicos da coluna (sem colocar as repetições)
    df_unique = df["col2"].unique()
    print(df_unique)
    #retorna o total de valores distintos
    df_nunique = df["col2"].nunique()
    print(df_nunique)
    #Permite a contagem da presença de cada valor na coluna (número de repetições por valor)
    df_vcount = df["col2"].value_counts()
    print(df_vcount)
    print("---")
    #Permite a obtenção de uma lista com valores distintos na coluna
    df_vcount_index = df["col2"].value_counts().index
    print(df_vcount_index)

    #Aplicando funções
    def comp(x):
        return x**2+3

    df_apply_comp = df["col1"].apply(comp)
    print("---")
    print(df_apply_comp)

    #Usando lambdas no apply (para o caso de funções simples)
    df_apply_lambda = df["col1"].apply(lambda x: x**2+3)
    print("---")
    print(df_apply_lambda)

    #Outras funções
    print(df["col1"].sum())
    print(df["col1"].mean())
    print(df["col1"].product())
    print(df["col1"].std())
    print(df["col1"].max())
    print(df["col1"].min())
    #índice do valor máximo
    print(df["col1"].idxmax())

    #Usando funções em filtros
    df_filtro = df[df["col2"] == 444]
    print('---')
    print(df_filtro)
    #Somatório dos elementos da col1 sob condição col2 = 444
    df_filtro_sum = df[df["col2"] == 444]["col1"].sum()
    print('---')
    print(df_filtro_sum)

    #Ordenação
    df_sort = df.sort_values(by="col2")
    print("---")
    print(df_sort)

    data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
            'B': ['one', 'one', 'two', 'two', 'one', 'one'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [1, 3, 2, 5, 4, 1]}

    #Mapeamento do dataframe
    df_2 = pd.DataFrame(data)

    #Substitui os valores da esquerda pelos da direita no map
    dicionario_map = {
        'foo': 'fu',
        'bar': 'bah',
    }
    #criação de coluna E usando o mapeamento acima sobre a coluna A
    df_2["E"] = df_2["A"].map(dicionario_map)
    print("---")
    print(df_2)

    #Pivot table - cria tabela com linhas = index e colunas = columns, usando a média dos valores correspondentes em values

    df_ptable = df_2.pivot_table(index="A", columns="B", values="D")
    print("----")
    print(df_ptable)

operacoes_dataframes()