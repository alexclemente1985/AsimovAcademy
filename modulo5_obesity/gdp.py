import datetime
from pathlib import Path

import pandas as pd


def gdp():
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    df_gdp = pd.read_csv(Path.joinpath(datasets, 'gdp.csv'), decimal='.')

    # PRIMEIRA QUESTÃO: Tratamento dos dados
    ##Verificação de informações básicas do dataframe
    print(df_gdp.info())
    print(df_gdp.columns.values)
    print(df_gdp['Country'].head(5))
    print(df_gdp['Region'].head(5))
    print(df_gdp['Year'].head(5))
    print(df_gdp[' GDP_pp '].head(5))
    ##Tratamento do nome da coluna GDP_pp -> alteração do nome para GDP
    df_gdp.rename(columns={' GDP_pp ': 'GDP'}, inplace=True)
    ###Verificação da alteração
    print('Verificando alteração do nome da coluna GDP_pp para GDP:')
    print(df_gdp.columns.values)
    print(df_gdp.info())
    print(df_gdp[['Year', 'GDP']])
    ##Verificação de nulos
    print(df_gdp.isnull().values.any())
    print(df_gdp.isna().values.any())
    print(df_gdp.isnull().value_counts())
    print(df_gdp.isna().value_counts())

    ## Conversão das colunas que representam valores numéricos para tipo int ou float
    ### Conversão Year para datetime e depois registrar apenas o ano, criando coluna para data completa
    df_gdp['Year'] = pd.to_datetime(df_gdp['Year'])
    df_gdp['Date'] = df_gdp['Year']
    df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.year))
    ### Conversão de GDP para float
    df_gdp['GDP'] = df_gdp['GDP'].apply(lambda x: float(x.replace(',', '').strip()))
    print(df_gdp.info())
    print(df_gdp[df_gdp['GDP'] > 1000][['Year', 'Date', 'GDP']].head(5))

    # SEGUNDA QUESTÃO: Primeiro valor registrado de cada país
    df_gdp_gpby_country = df_gdp.groupby('Country')
    print(df_gdp_gpby_country[['Year']].min())

    # TERCEIRA QUESTÃO: Regiões com maiores crescimentos de PIB per capita do século passado
    ## Nota: Século inicia em um ano com final 01 e termina em um ano com final 00 -> Ex: Século XX - início em 1901 | término em 2000
    df_gdp_year_idx = df_gdp.set_index(["Year"])
    df_gdp_region = df_gdp_year_idx[(df_gdp_year_idx.index > 1901) & (df_gdp_year_idx.index < 2000)].set_index(['Region'])
    print(df_gdp_region.sort_values(by="GDP", ascending=False).head(5))


gdp()
