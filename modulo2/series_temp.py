import datetime

import pandas as pd


def series_temp():
    #Séries temporais: dataframe onde cada linha representa um conjunto de informações a cada momento

    numero_dias = 100
    datas = pd.date_range(start='1/1/2021', periods=numero_dias)

    print(datas)
    #Criação de df indexado com as datas criadas no passo anterior
    df = pd.DataFrame(range(numero_dias), columns=["number"], index=datas)

    #Acessando informações de tempo de cada registro
    print(df)
    print(df.index[0])
    print(df.index[0].day)
    print(df.index[0].month)
    print(df.index[0].year)
    print(df.index[0].hour)

    #Fazendo filtros com as informações de tempo
    df_dia_10 = df[df.index.day == 10]
    print(df_dia_10)
    #Criando novas colunas no df usando informações de tempo
    df["Month"] = df.index.month
    print("Novo DF")
    print(df)
    #Filtro para obtenção de dados com tempo superior a uma data específica
    df_datetime = df[df.index > datetime.datetime(2021,1,10)]
    print("df_datetime")
    print(df_datetime)

series_temp()