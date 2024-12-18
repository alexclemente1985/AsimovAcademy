import pandas as pd
from pathlib import Path

def dataset():
    data = Path.joinpath(Path.cwd(), 'data', 'cleaned_data.csv')
    df_data = pd.read_csv(data, index_col=0)

    mean_lat = df_data['LATITUDE'].mean()
    mean_long = df_data['LONGITUDE'].mean()

    #Tratamento dos dados
    
    ##Conversão de pés quadrados para metros quadrados
    df_data['size_m2'] = df_data['GROSS SQUARE FEET']/10.764

    ##Remoção de imóveis sem ano definido
    df_data = df_data[df_data['YEAR BUILT']>0]

    ##Pré-processamento de SALE DATE para datetime ao invés de objeto (string)
    df_data['SALE DATE'] = pd.to_datetime(df_data['SALE DATE'])

    ##Ajustes gerais de metragem (limitação de tamanhos para evitar ver pontos muito gigantescos no mapa)
    df_data.loc[df_data['size_m2'] > 10000, 'size_m2'] = 10000
    df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000
    df_data.loc[df_data['SALE PRICE'] < 100000, 'SALE PRICE'] = 100000

    return df_data, mean_lat, mean_long
    


dataset()