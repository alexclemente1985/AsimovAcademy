import pandas as pd
from numpy.random import randn


def dataframes():
    #Dataframe -> conjunto de Series
    df = pd.DataFrame(randn(5, 4), index=["A", "B", "C", "D", "E"], columns="W Y X Z".split())

    print(df)

    #Especificando colunas no formato Serie
    print(df['W'])
    ##Especificando coluna no formato Dataframe
    print(df[['W']])

    #Criando colunas a partir de outras (cópias)
    df["New"] = df["W"] + df["Y"]
    print(df)

    #Removendo colunas
    df_sem_new = df.drop("New", axis=1)
    print(df_sem_new)

    #Removendo colunas do DF original
    df.drop("New", axis=1, inplace=True)
    print(df)

    #Acessando linhas do Dataframe
    ##Serie com colunas = indices
    print(df.loc['A'])
    ##Representação como Dataframe
    print(df.loc[['D']])
    print(df.loc[['A','B']])

    #Trabalhando os valores de linhas e colunas por meio dos indices numéricos
    print(df.iloc[[1,2]])

dataframes()
