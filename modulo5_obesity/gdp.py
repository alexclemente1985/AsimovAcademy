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
    df_gdp_idx_year = df_gdp.sort_values(by="Year").set_index(["Year"])[["Region", "GDP"]]
    df_gdp_20_century = df_gdp_idx_year[(df_gdp_idx_year.index >= 1901) & (df_gdp_idx_year.index <= 2000)]

    initial_year = df_gdp_20_century.index.min()
    final_year = df_gdp_20_century.index.max()

    df_gdp_20_cent_start = df_gdp_20_century[df_gdp_20_century.index == initial_year].groupby("Region").mean()
    df_gdp_20_cent_final = df_gdp_20_century[df_gdp_20_century.index == final_year].groupby("Region").mean()

    print(df_gdp_20_cent_start)
    print(df_gdp_20_cent_final)

    df_gdp_20_cent_mean_var = pd.merge(df_gdp_20_cent_start, df_gdp_20_cent_final, on=["Region"],
                                       suffixes=(f"_Mean {initial_year}", f"_Mean {final_year}"))


    df_gdp_20_cent_mean_var['Variation (%)'] = ((df_gdp_20_cent_mean_var['GDP_Mean 1996'] / df_gdp_20_cent_mean_var[
        'GDP_Mean 1901']) - 1) * 100
    print(df_gdp_20_cent_mean_var.sort_values(by='Variation (%)', ascending=False))

    #Resposta do professor adaptada ao que já tinha sido feito aqui
    df_gdp_20_cent_var = (((df_gdp_20_cent_final / df_gdp_20_cent_start) - 1) * 100).sort_values(by="GDP",
                                                                                                 ascending=False)
    print(df_gdp_20_cent_var)

    #QUARTA QUESTÃO: Preencha dados ausentes de cada país com estimativas baseadas na diferença entre registros anteriores e posteriores do país

    print(df_gdp)


gdp()
