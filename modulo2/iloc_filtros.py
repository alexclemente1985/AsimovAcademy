import pandas as pd
from numpy.random import randn


def iloc_filtros():
    # Dataframe -> conjunto de Series
    df = pd.DataFrame(randn(5, 4), index=["A", "B", "C", "D", "E"], columns="W Y X Z".split())
    #Filtro por linhas
    print(df.loc[['A', 'B']])
    # Filtro por linhas especificando coluna
    print(df.loc[['A', 'B'], ["W"]])
    # Filtro por linhas através de indice (todas as linhas exceto a última, todas as colunas a partir da segunda)
    print(df.iloc[:-1, 1:])
    # Filtro por linhas através de indice (linha 1 até 3, coluna 1 até 2)
    print(df.iloc[1:4, 1:3])

    #Filtros condicionais
    ## Mostra tabela onde cada posição é substituída pelo bool do valor na condição
    print(df > 0)
    ## Mostra tabela onde somente valores na condição são mostrados (demais NaN)
    print(df[df>0])
    ## Mostra Serie baseada na coluna Y, onde cada posição é subst. pelo bool do valor na condição
    print(df["Y"] > 0)
    ## Mostra tabela somente com as linhas que satisfaçam a condição na coluna Y
    print(df[df["Y"] > 0])
    ## Mostra tabela somente com as linhas que satisfaçam a condição na coluna Y e W ao mesmo tempo
    print(df[((df["Y"] > 0) & (df["W"] > 0))])

iloc_filtros()