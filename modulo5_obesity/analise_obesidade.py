from pathlib import Path

import pandas as pd
import numpy as np


def analise_obesidade():
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    data_obesity = pd.read_csv(Path.joinpath(datasets, 'obesity_cleaned.csv'))

    print(data_obesity.info())
    print(data_obesity.head())

    # >>>>>Funções extras para auxiliar a realização dos exercícios<<<<<

    ##to_frame() ou []
    print(data_obesity[["Sex"]])
    print(data_obesity["Sex"].to_frame())

    ##transpose (matriz transposta)
    print(data_obesity["Sex"].to_frame().transpose())

    ##shift -> deslocamento de todos os valores uma célula abaixo, descartando o último valor
    ###util no cálculo entre valores de mesma coluna
    ### valores negativos: deslocamento para cima
    print(data_obesity["Sex"].to_frame().shift(1))
    ## isin() -> retorna elementos True False caso possuirem valores iguais aos informados
    print(data_obesity["Year"].to_frame().isin([1900, 1901, 1975]))

    ##values | index | columns-> cria array a partir da coluna (redução de gasto computacional na operação)
    print(data_obesity["Sex"].values)
    print(data_obesity.index)
    print(data_obesity.columns)

    ##iterrows() permite iteração com os valores do dataframe
    for idx, row in data_obesity.iterrows():
        print(idx, row['Country'])
        if idx == 5:
            break

    # to_dict() Cria mapeamento e permite criação e preenchimento de novas colunas ou dataframes
    ##Nota: util para resolução da questão da obesidade com Per capita
    print(data_obesity.set_index("Year").head())
    print(data_obesity.set_index("Year").to_dict().keys())

    print(data_obesity.set_index("Year").to_dict()["Country"])

    # >>>>>>>FIM FUNÇÕES EXTRAS<<<<<<<

    # >>>ATIVIDADE AULA<<<

    # Verificação de repetições de valores e situação geral da coluna de obesidade
    print(data_obesity['Obesity (%)'].value_counts())
    # Verificação dos retornos onde obesidade = 'No data' -> 504 registros
    print(data_obesity[data_obesity['Obesity (%)'].apply(lambda x: x.strip() == 'No data')])

    # Criação de coluna Obesity
    df_obesidade = pd.DataFrame()

    # Verificação das colunas do dataframe original
    print(data_obesity.columns)

    # Obtenção das colunas do dataframe original exceto a 'Unnamed: 0'
    columns = [col for col in data_obesity.columns if col != 'Unnamed: 0']
    print('Colunas do dataframe: \n', columns)

    # Preenchimento do dataframe de estudo com as colunas necessárias do original
    df_obesidade[columns] = data_obesity[columns]

    # Renomeação da coluna de obesidade para o nome solicitado no exercício
    df_obesidade.rename(columns={'Obesity (%)': 'Obesity'}, inplace=True)
    print('df obesidade info inicial')
    print(df_obesidade.info())

    # Alteração dos valores da coluna obesidade para pegar os percentuais sem a faixa de valores
    df_obesidade['Obesity'] = df_obesidade['Obesity'].apply(lambda x: x.split(' ')[0])
    print('Valores alterados com split na coluna de obesidade: ')
    print(df_obesidade.head())

    # Remoção dos valores 'No' que sobraram do split de 'No data'
    index_no = df_obesidade[df_obesidade['Obesity'] == 'No'].index
    print('Lista de índices dos valores "No": \n', index_no)
    df_obesidade.drop(index_no, inplace=True)
    print("dataframe de estudo após remoção dos valores 'No'")
    print(df_obesidade.value_counts())
    print(df_obesidade.info())
    # Conversão dos valores em float e verificação do resultado
    df_obesidade['Obesity'] = df_obesidade['Obesity'].apply(lambda x: float(x))
    print("Situação do dataframe de estudo após conversão dos valores de obesidade para float: ")
    print(df_obesidade.info())
    print(df_obesidade.head())

    ##>>>Professor: converteu todos em nan e depois usou dropna
    ### df_obesidade.loc[df_obesidade['Obesity'] == 'No', 'Obesity'] = np.nan
    ### df_obesidade.dropna()

    # SEGUNDA QUESTÃO-> PERCENTUAL MÉDIO DE OBESIDADE POR SEXO NO MUNDO EM 2015


analise_obesidade()
