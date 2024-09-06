from pathlib import Path

import pandas as pd
import numpy as np


def analise_obesidade():
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    data_obesity = pd.read_csv(Path.joinpath(datasets, 'obesity_cleaned.csv'))

    print(data_obesity.info())
    print(data_obesity.head())

    #>>>>>Funções extras para auxiliar a realização dos exercícios<<<<<

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
    print(data_obesity["Year"].to_frame().isin([1900,1901,1975]))

    ##values | index | columns-> cria array a partir da coluna (redução de gasto computacional na operação)
    print(data_obesity["Sex"].values)
    print(data_obesity.index)
    print(data_obesity.columns)

    ##iterrows() permite iteração com os valores do dataframe
    for idx, row in data_obesity.iterrows():
        print(idx, row['Country'])
        if idx == 5:
            break

    #to_dict() Cria mapeamento e permite criação e preenchimento de novas colunas ou dataframes
    ##Nota: util para resolução da questão da obesidade com Per capita
    print(data_obesity.set_index("Year").head())
    print(data_obesity.set_index("Year").to_dict().keys())

    print(data_obesity.set_index("Year").to_dict()["Country"])


analise_obesidade()
