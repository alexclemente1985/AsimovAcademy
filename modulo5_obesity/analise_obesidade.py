from pathlib import Path

import pandas as pd
import numpy as np
import plotly.graph_objects as go


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
    df_obesidade['Year'] = df_obesidade["Year"].apply(lambda x: int(x))
    ##Criação do index com Year
    df_obesidade.set_index("Year", inplace=True)
    print("Situação do dataframe de estudo após conversão dos valores de obesidade para float: ")
    print(df_obesidade.info())
    print(df_obesidade.head())

    ##>>>Professor: converteu todos em nan e depois usou dropna
    ### df_obesidade.loc[df_obesidade['Obesity'] == 'No', 'Obesity'] = np.nan
    ### df_obesidade.dropna()

    # SEGUNDA QUESTÃO-> PERCENTUAL MÉDIO DE OBESIDADE POR SEXO NO MUNDO EM 2015
    df_ob_2015 = df_obesidade[df_obesidade.index == 2015]

    df_ob_2015_sex = df_ob_2015[["Sex", "Obesity"]]

    df_ob_2015_sex_mean = df_ob_2015_sex.groupby("Sex").mean()
    df_ob_2015_sex_mean["Obesity"] = df_ob_2015_sex_mean["Obesity"].apply(lambda x: f'{round(x, 2)}%')
    df_ob_2015_sex_mean.rename(columns={"Obesity": "Average Obesity in 2015"}, inplace=True)
    print(df_ob_2015_sex_mean)

    # TERCEIRA QUESTÃO -> 5 PAÍSES COM MAIOR E MENOR TAXA DE AUMENTO DOS ÍNDICES DE OBESIDADE NO PERÍODO TOTAL

    min_year = df_obesidade.index.min()
    max_year = df_obesidade.index.max()
    print('TERCEIRA QUESTÃO')
    print(min_year, max_year)

    # Verificação da existência de nulos no período
    df_ob_both = df_obesidade[df_obesidade["Sex"] == "Both sexes"]
    print(df_ob_both.isnull().values.any())
    print(df_ob_both.isna().values.any())

    print(df_ob_both)
    df_ob_var_end = df_ob_both[df_ob_both.index == max_year]
    df_ob_var_start = df_ob_both[df_ob_both.index == min_year]

    print(df_ob_var_start)
    print(df_ob_var_end)

    df_var = pd.merge(
        df_ob_var_start[df_ob_var_start.columns.difference(['Sex'])],
        df_ob_var_end[df_ob_var_end.columns.difference(['Sex'])],
        how="inner",
        on=['Country'],
        suffixes=(f" {min_year}", f" {max_year}"))

    df_var.set_index(['Country'], inplace=True)
    print(df_var)
    df_var["Abs Ob Var"] = df_var["Obesity 2016"] - df_var["Obesity 1975"]
    df_var["Ob Variation (%)"] = round(((df_var["Obesity 2016"] / df_var["Obesity 1975"]) - 1) * 100, 2)

    print(df_var[['Abs Ob Var', 'Ob Variation (%)']].sort_values(ascending=False, by='Abs Ob Var').head(5))
    print(df_var[['Abs Ob Var', 'Ob Variation (%)']].sort_values(by='Abs Ob Var').head(5))

    # QUARTA QUESTÃO -> PAÍSES COM MAIORES E MENORES NÍVEIS PERCENTUAIS DE OBESIDADE EM 2015

    print('\nQUARTA QUESTÃO')
    # Considerando apenas 'Both sexes'
    df_ob_2015 = (df_obesidade[
                      (df_obesidade.index == 2015) & (df_obesidade['Sex'] == 'Both sexes')
                      ][df_obesidade.columns.difference(['Sex'])]
                  .copy()
                  .set_index("Country")
                  .sort_values(by="Obesity"))

    print(df_ob_2015.head(1))
    print(df_ob_2015.tail(1))

    # Considerando 'Male' e 'Female'
    df_ob_2015 = df_obesidade[(df_obesidade.index == 2015) & (df_obesidade['Sex'] != 'Both sexes')
                              ].copy().set_index("Country").sort_values(by="Obesity")

    print(df_ob_2015.head(1))
    print(df_ob_2015.tail(1))

    print("\nSolução do professor ----------------")
    df_2015 = df_obesidade[df_obesidade.index == 2015].copy()
    print('\n Máximos')
    print(df_2015[df_2015["Obesity"] == df_2015["Obesity"].max()])
    print('\n Mínimos')
    print(df_2015[df_2015["Obesity"] == df_2015["Obesity"].min()])

    # QUINTA QUESTÃO: DIFERENÇA MÉDIA PERCENTUAL OB AO LONGO DOS ANOS ENTRE SEXOS BRASIL
    print('\nQUINTA QUESTÃO')
    df_ob_brazil = df_obesidade[(df_obesidade['Country'] == 'Brazil') & (df_obesidade['Sex'] != 'Both sexes')].copy()
    df_ob_brazil_diff = pd.DataFrame()
    df_ob_brazil_diff['Brazil Obesity Genre Difference (%)'] = df_ob_brazil[df_ob_brazil['Sex'] == 'Male'][
                                                                   ['Obesity']] - \
                                                               df_ob_brazil[df_ob_brazil['Sex'] == 'Female'][
                                                                   ['Obesity']]
    df_ob_brazil_diff['Brazil Obesity Genre Difference (%)'] = df_ob_brazil_diff[
        'Brazil Obesity Genre Difference (%)'].apply(lambda x: abs(x))

    print(df_ob_brazil_diff)

    print("\nDiferença média percentual de obesidade entre sexos ao longo dos anos no Brasil:")
    print(f"{round(df_ob_brazil_diff['Brazil Obesity Genre Difference (%)'].mean(), 2)}%")

    fig = go.Figure(data=go.Scatter(
        x=df_ob_brazil_diff.index,
        y=df_ob_brazil_diff['Brazil Obesity Genre Difference (%)'],
        mode="lines+markers",
        hovertemplate="Diferença entre Obesidades: %{y}% | Ano: %{x}",
        name="Diferença Percentual entre Gêneros",
        marker=dict({'color': 'purple'})
    ))

    fig.update_layout(title_text='Diferença Percentual de Obesidades entre Gêneros no Brasil',
                      yaxis_title="Diferenças Percentuais entre Gêneros (%)", xaxis_title="Anos")

    fig.add_trace(go.Scatter(x=df_ob_brazil.query("Sex=='Male'").index,
                             y=df_ob_brazil.query("Sex=='Male'")['Obesity'],
                             mode="lines+markers",
                             hovertemplate="Obesidade: %{y}% | Ano: %{x}",
                             name="Percentual Anual de Obesidade: Homens",
                             marker=dict({'color': 'orange'})
                             ))

    fig.add_trace(go.Scatter(x=df_ob_brazil[df_ob_brazil['Sex'] == 'Female'].index,
                             y=df_ob_brazil[df_ob_brazil['Sex'] == 'Female']['Obesity'],
                             mode="lines+markers",
                             hovertemplate="Obesidade: %{y}% | Ano: %{x}",
                             name="Percentual Anual de Obesidade: Mulheres",
                             marker=dict({'color': 'pink'})
                             ))

    fig.show()
    print(df_ob_brazil[df_ob_brazil['Sex'] == 'Male']['Obesity'])

    # SEXTA QUESTÃO: GRÁFICO DE EVOLUÇÃO DA OBESIDADE DE AMBOS OS SEXOS NO MUNDO
    df_ob_both = df_obesidade[df_obesidade['Sex'] == 'Both sexes'][df_ob_both.columns.difference(['Sex'])]

    print(df_ob_both)
    df_ob_both.reset_index(inplace=True)
    print(df_ob_both)
    #Criar groupby apenas com Year e fazer mean() com Obesity
    df_ob_both_mean = df_ob_both.groupby('Year')['Obesity'].mean()
    df_ob_both_mean.rename("Média", inplace=True)

    print(df_ob_both_mean)

    fig2 = go.Figure(data=go.Scatter(x=df_ob_both_mean.index, y=df_ob_both_mean))
    fig2.update_layout(title_text='Médias de Obesidades no Mundo',
                      yaxis_title="Obesidade Média (%)", xaxis_title="Anos")
    fig2.show()


analise_obesidade()
