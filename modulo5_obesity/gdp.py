import datetime
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import plotly.express as px


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
    # df_gdp['Date'] = df_gdp['Year']
    df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.year))
    ### Conversão de GDP para float
    df_gdp['GDP'] = df_gdp['GDP'].apply(lambda x: float(x.replace(',', '').strip()))
    print(df_gdp.info())
    # print(df_gdp[df_gdp['GDP'] > 1000][['Year', 'Date', 'GDP']].head(5))

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

    # Resposta do professor adaptada ao que já tinha sido feito aqui
    df_gdp_20_cent_var = (((df_gdp_20_cent_final / df_gdp_20_cent_start) - 1) * 100).sort_values(by="GDP",
                                                                                                 ascending=False)
    print(df_gdp_20_cent_var)

    # QUARTA QUESTÃO: Preencha dados ausentes de cada país com estimativas baseadas na diferença entre registros anteriores e posteriores do país

    print(df_gdp)

    ##1) Obtenção da sequência de anos do período
    start_year, final_year = df_gdp["Year"].min(), df_gdp["Year"].max()
    print(start_year, final_year)

    # lista de anos no período total
    gdp_all_years_list = list(range(start_year, final_year, 1))

    # lista de países
    gdp_all_countries_list = list(set(df_gdp['Country']))
    gdp_all_countries_list.sort()

    # Obtenção das taxas de crescimento dos períodos não registrados, de acordo com a diferença entre os valores max e min do período
    df_gdp.sort_values(["Country", "Year"], inplace=True)
    ## NOTA: shift(n) -> desloca todas as linhas do dataframe "n" índices acima, permitindo operações do registro atual com anteriores (USADO NA QUESTÃO)
    ### shift(-n) -> desloca todas as linhas do dataframe "n" índices abaixo, permitindo operações do registro atual com posteriores
    df_gdp["Delta_GDP"] = df_gdp["GDP"] - df_gdp["GDP"].shift(1)
    # NOTA: Observa-se que os dados foram coletados de 5 em 5 anos, de acordo com a operação abaixo
    df_gdp["Delta_Year"] = df_gdp["Year"] - df_gdp["Year"].shift(1)

    ## Taxa de crescimento
    ### Nota: Uso do shift(-1) permite guardar o valor do coeficiente de variação do período no registro do início do período, facilitando o cálculo das estimativas
    df_gdp["Coeficiente_GDP_Year"] = (df_gdp["Delta_GDP"] / df_gdp["Delta_Year"]).shift(-1)

    ## Remoção das colunas de delta
    del df_gdp["Delta_GDP"], df_gdp["Delta_Year"]

    # dataframe para juntar total de países com total de anos
    df_all_countries_all_years = pd.DataFrame(columns=["Country", "Year"])

    # Preenchimento da tabela que permitirá a estimativa dos valores ausentes, com todos os países e todos os anos
    # for idx, c in df_all_countries.iterrows():
    for c in gdp_all_countries_list:
        for y in gdp_all_years_list:
            # add_row = c.copy()
            # add_row["Year"] = y
            tmp_df = pd.DataFrame(columns=["Country", "Year"])
            tmp_df["Country"] = [c]
            tmp_df["Year"] = [y]

            df_all_countries_all_years = pd.concat([df_all_countries_all_years, tmp_df])
            # df_all_countries_all_years = pd.concat([df_all_countries_all_years, add_row.to_frame().transpose()])

    # Merge da tabela criada com a tabela original com os dados de GDP (merge de todos os dados)
    df_all_countries_all_years_merged = pd.merge(df_all_countries_all_years, df_gdp, on=["Country", "Year"],
                                                 how="outer")

    # Atualização da tabela mergeada com os dados estimados
    registered_year = 0
    coef = 0
    gdp = 0
    for idx, row in df_all_countries_all_years_merged.iterrows():
        if row["Year"] == 2011:
            if not pd.isna(row["GDP"]):
                df_all_countries_all_years_merged.at[idx, "Kind"] = "Real"
            continue

        if not pd.isna(row["GDP"]):
            registered_year = row["Year"]
            coef = row["Coeficiente_GDP_Year"]
            gdp = row["GDP"]
            df_all_countries_all_years_merged.at[idx, "Kind"] = "Real"
        else:
            ## Nota: O valor do GDP foi calculado baseado na fórmula da tangente -> t = coef. angular = (y-y0)/(x-x0) = (GDP - GDP0)/(year - year0)
            ### => GDP = (year - year0)*coef + GDP0
            df_all_countries_all_years_merged.at[idx, "GDP"] = (row["Year"] - registered_year) * coef + gdp
            df_all_countries_all_years_merged.at[idx, "Kind"] = "Estimated"

    # Criação de índice com coluna Year, com backup da coluna
    df_all_countries_all_years_merged["Year_tmp"] = df_all_countries_all_years_merged["Year"]
    df_all_countries_all_years_merged.set_index(["Year"], inplace=True)
    df_all_countries_all_years_merged.rename(columns={"Year_tmp": "Year"}, inplace=True)

    # Visualização da tabela final
    print(df_all_countries_all_years_merged[["Country", "Year", "GDP", "Kind"]].head(100))
    print(df_all_countries_all_years_merged[["Country", "Year", "GDP", "Kind"]].tail(100))

    fig, ax = plt.subplots(figsize=(20, 5))
    df_all_countries_all_years_merged[(df_all_countries_all_years_merged["Kind"] == "Real") & (
            df_all_countries_all_years_merged["Country"] == "United States")].plot(kind="scatter", y="GDP",
                                                                                   x="Year", ax=ax)
    df_all_countries_all_years_merged[(df_all_countries_all_years_merged["Kind"] == "Estimated") & (
            df_all_countries_all_years_merged["Country"] == "United States")].plot(kind="scatter", y="GDP",
                                                                                   x="Year", ax=ax, color="red")

    #plt.show()

    # Desafios

    ##Desafio 1 - Mapa do PIB ao longo dos anos

    df = px.data.gapminder()
    print(df.columns)
    dict_iso_alpha = df.set_index("country").to_dict()["iso_alpha"]
    dict_num = {j: i for i, j in enumerate(df_all_countries_all_years_merged["Country"].unique())}

    print(df_all_countries_all_years_merged["Country"].unique())

    df_all_countries_all_years_merged["iso_alpha"] = df_all_countries_all_years_merged["Country"].map(dict_iso_alpha)
    df_all_countries_all_years_merged["iso_num"] = df_all_countries_all_years_merged["Country"].map(dict_num)

    print(df_all_countries_all_years_merged)

    fig = px.choropleth(df_all_countries_all_years_merged[df_all_countries_all_years_merged["Kind"] == "Real"].reset_index(drop=True), locations="iso_alpha", color="GDP",
                        hover_name="Country", animation_frame="Year")

    fig.update_layout(height=600)
    fig.show()
    plt.close()

    # Desafio 2 - Relação GDP e Obesidade
    df_obesity = pd.read_csv(Path.joinpath(datasets, 'obesity_cleaned.csv'))

    del df_obesity["Unnamed: 0"]
    df_obesity.rename(columns={'Obesity (%)': 'Obesity'}, inplace=True)
    df_obesity['Obesity'] = df_obesity['Obesity'].apply(lambda x: x.split(' ')[0])
    index_no = df_obesity[df_obesity['Obesity'] == 'No'].index
    df_obesity.drop(index_no, inplace=True)
    df_obesity['Obesity'] = df_obesity['Obesity'].apply(lambda x: float(x))
    df_obesity['Year'] = df_obesity["Year"].apply(lambda x: int(x))
    df_obesity.set_index("Year", inplace=True)

    df_obesity['country-year'] = df_obesity["Country"] + "-" + df_obesity.reset_index()["Year"].apply(lambda x: str(int(x))).values


    print(df_obesity.columns)
    dict_obesity_year = df_obesity.set_index("country-year").to_dict()["Obesity"]

    df_all_countries_all_years_merged["country-year"] = df_all_countries_all_years_merged["Country"] + "-" + df_all_countries_all_years_merged["Year"].apply(lambda x: str(x)).values
    df_all_countries_all_years_merged["Obesity"] = df_all_countries_all_years_merged["country-year"].map(dict_obesity_year)

    df_gdp_clean = df_all_countries_all_years_merged.dropna()

    countries = df_gdp_clean["Country"].unique()

    corr_list = []
    for country in countries:
        corr_list += [df_gdp_clean[df_gdp_clean["Country"] == country][["Obesity", "GDP"]].corr().iloc[0, 1]]

    df_corr = pd.Series(corr_list, index=countries)
    print(df_corr)

    print(df_corr.mean())
    print(df_corr.std())

    df_corr.sort_values().plot()
    plt.show()

    country = "Australia"
    fig, ax = plt.subplots()
    df_gdp_clean[df_gdp_clean["Country"] == country][["Obesity"]].plot(ax=ax)
    ax2 = ax.twinx()
    df_gdp_clean[df_gdp_clean["Country"] == country][["GDP"]].plot(ax=ax2, color="red")

    plt.show()

    print(df_gdp_clean[df_gdp_clean["Country"]==country][["Country","Obesity","GDP"]])

    #Cálculo da relação entre obesidade e gdp
    print(df_gdp_clean.reset_index(drop=True).groupby("Year")[["Obesity", "GDP"]].mean().corr().iloc[0, 1])


gdp()
