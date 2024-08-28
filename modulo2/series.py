import pandas as pd
from pathlib import Path
import numpy as np


def series():
    datasets = Path.joinpath(Path.cwd().parent, 'datasets')
    df_data = pd.read_csv(Path.joinpath(datasets, 'supermarket_sales.csv'))

    print(df_data)

    labels = ['a', 'b', 'c']
    minha_lista = [10, 20, 30]
    arr = np.array(minha_lista)

    d = dict()

    for i in range(len(labels)):
        d[labels[i]] = minha_lista[i]

    print(d)

    # Serie -> igual a lista, porém visualizada com indice (padrão igual posição na lista)
    series_pd = pd.Series(labels)
    print(series_pd)
    print(series_pd[2])

    #Serie com index personalizado
    series_pd_idx = pd.Series(data=labels, index=minha_lista)

    print(series_pd_idx)

    #Serie criada por dicionário
    series_dict = pd.Series(d)
    print(series_dict)

    # Seleção de indices da serie
    series_paises = pd.Series([1,2,3,4], index=['EUA','Alemanha', 'USSR', 'Japão'])
    print(series_paises)
    series_paises2 = pd.Series([1, 2, 5, 4], index=['EUA', 'Alemanha', 'Italia', 'Japão'])
    print(series_paises2)

    print(series_paises['EUA'])
    print(series_paises[['EUA', 'USSR']])

    # Soma aritmética de series (indices não pareados irão retornar NaN)
    print(series_paises + series_paises2)



series()
