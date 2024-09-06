import pandas as pd
from pathlib import Path


def analise_gasolina():
    # Caminho dataset
    dataset = Path.joinpath(Path.cwd(), 'datasets')
    # Carregamento dos dados csv de gasolina
    data_2000 = pd.read_csv(Path.joinpath(dataset, 'gasolina_2000+.csv'), index_col=0)
    data_2010 = pd.read_csv(Path.joinpath(dataset, 'gasolina_2010+.csv'), index_col=0)

    print("DATA 2000")
    print(data_2000)
    print("DATA 2010")
    print(data_2010)

    print(data_2010.info)
    # Criando dataframe com o concatenado dos dados
    data = pd.concat([data_2000, data_2010])
    print(data)

    df = pd.DataFrame(data)
    # Verificando informações HEAD e INFO
    print("HEAD")
    print(df.head())
    print("INFO")
    print(df.info())

    # Verificando terceira entrada da coluna DATA INICIAL e convertendo ela e DATA FINAL em datetime
    print("Terceira entrada coluna DATA INICIAL")
    print(df['DATA INICIAL'].iloc[2], type(df['DATA INICIAL'].iloc[2]))

    # df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
    df[['DATA INICIAL', 'DATA FINAL']] = df[['DATA INICIAL', 'DATA FINAL']].apply(pd.to_datetime)
    print(df['DATA INICIAL'].iloc[2], type(df['DATA INICIAL'].iloc[2]))
    print(df['DATA FINAL'].iloc[2], type(df['DATA FINAL'].iloc[2]))

    # Criando coluna ANO MES usando DATA FINAL como referência
    df['ANO-MES'] = df['DATA FINAL'].dt.strftime('%Y-%m')
    # Solução professor (muito extensa)
    # df["ANO-MES"] = df["DATA FINAL"].apply(lambda x: "{}".format(x.year)) + df["DATA FINAL"].apply(lambda x: "-{:02d}".format(x.month))
    print('Ano Mes')
    print(df['ANO-MES'].iloc[2], type(df['ANO-MES'].iloc[2]))

    # Value counts
    print(df['PRODUTO'].value_counts())

    # FILTRO GASOLINA COMUM
    df_gas_comum = df[df['PRODUTO'] == 'GASOLINA COMUM']
    print(df_gas_comum.head())

    # Preço médio revenda gasolina comum agosto 2008
    df_agosto2008 = df_gas_comum[df_gas_comum['ANO-MES'] == '2008-08']
    print(f"Preço médio gasolina comum Agosto 2008: R$ {df_agosto2008['PREÇO MÉDIO REVENDA'].mean():.2f}")

    # Preço médio de revenda da gasolina em maio de 2014 em São Paulo
    df_maio2014_SP = df_gas_comum[(df_gas_comum['ANO-MES'] == '2014-05') & (df_gas_comum['ESTADO'] == 'SAO PAULO')]
    print(f"Preço médio gasolina comum Maio 2014 em SP: R$ {df_maio2014_SP['PREÇO MÉDIO REVENDA'].mean():.2f}")

    # Quais estados a gasolina superou R$ 5.00 e quando isso ocorreu
    df_gas_maior_5 = df_gas_comum[df_gas_comum['PREÇO MÉDIO REVENDA'] > 5]
    print(df_gas_maior_5[['ESTADO', 'DATA FINAL']])
    print(df_gas_maior_5[['ESTADO', 'ANO-MES', 'PREÇO MÉDIO REVENDA']])

    # MÉDIA DE PREÇOS DOS ESTADOS DA REGIÃO SUL EM 2012
    df_regiao_sul2012_preco_medio_mean = \
        df_gas_comum[(df_gas_comum['REGIÃO'] == 'SUL') & (df_gas_comum["DATA FINAL"].apply(lambda x: x.year) == 2012)][
            'PREÇO MÉDIO REVENDA'].mean()
    df_regiao_sul2012_groupby_estado = \
        df_gas_comum[(df_gas_comum['REGIÃO'] == 'SUL') & (df_gas_comum["DATA FINAL"].apply(lambda x: x.year) == 2012)][
            ['ESTADO', 'PREÇO MÉDIO REVENDA']].groupby('ESTADO')
    print(f"Preço médio de cada estado região SUL: \n{df_regiao_sul2012_groupby_estado.mean()}")
    print(f"Preço médio total da região SUL: {df_regiao_sul2012_preco_medio_mean}")

    # Tabela com variação percentual anual estado do RJ
    df_estado_rj = df_gas_comum[df_gas_comum['ESTADO'] == 'RIO DE JANEIRO']
    print(df_estado_rj.head())
    df_rj_tabela = df_estado_rj[['ANO-MES', 'PREÇO MÉDIO REVENDA', 'DATA FINAL']]
    df_rj_tabela['ANO'] = df_rj_tabela['DATA FINAL'].apply(lambda x: x.year)
    df_rj_tabela['MES'] = df_rj_tabela['DATA FINAL'].apply(lambda x: x.month)
    print("Tabela de coeficientes de variação de preço no RJ: ")
    print(df_rj_tabela)

    df_rj_tabela_groupby = df_rj_tabela.groupby('ANO')[['PREÇO MÉDIO REVENDA', 'MES']].last()
    print(df_rj_tabela_groupby)

    df_rj_tabela_var_anual = df_rj_tabela_groupby[df_rj_tabela_groupby['MES'] == 12]
    print(df_rj_tabela_var_anual)
    ##NOTA: shift(n) pega o valor do registro n posições antes do registro atual... no caso, pegou da posição anterior para fazer a variação anual
    ###Pode-se melhorar a tabela, pois o processo abaixo está fazendo o mesmo com a coluna MES (o que não tem sentido)
    df_rj_variacoes = (df_rj_tabela_var_anual / df_rj_tabela_var_anual.shift(1) - 1) * 100
    print(df_rj_variacoes[['PREÇO MÉDIO REVENDA']])

    # Série temporal
    print(df_gas_comum)
    # Criação série temporal
    df_gas_max_min = df_gas_comum[
        ['ANO-MES', 'PREÇO MÉDIO REVENDA', 'PREÇO MÁXIMO REVENDA', 'PREÇO MÍNIMO REVENDA', 'ESTADO']]
    print(df_gas_max_min.head())
    df_gas_max_min_gpby = df_gas_max_min.groupby('ANO-MES')
    print(df_gas_max_min_gpby.head())

    print('--------')
    # Criação das colunas de máximos e mínimos para cada período, e colunas para os respectivos índices

    df_max = df_gas_max_min_gpby.max()['PREÇO MÁXIMO REVENDA']
    df_min = df_gas_max_min_gpby.min()['PREÇO MÍNIMO REVENDA']
    idx_max = df_gas_max_min_gpby['PREÇO MÁXIMO REVENDA'].idxmax()
    idx_min = df_gas_max_min_gpby['PREÇO MÍNIMO REVENDA'].idxmin()

    # Criação do DataFrame que irá comportar todos os dados necessários
    df_diff = pd.DataFrame()

    # Criação das colunas de variações abs e perc, e com valores de máx e min

    df_diff['ABS_DIFF'] = df_max - df_min
    df_diff['PERC_DIFF'] = (df_max - df_min) / df_min * 100
    df_diff['MAX'] = df_max
    df_diff['MIN'] = df_min
    print(df_diff)

    # Verificação na tabela original quanto à localização de dados de estado com valor máximo,
    ## verificando todas as colunas (:) nos registros de índices de máximo (idx_max)
    print(df_gas_max_min.loc[idx_max, :][['ESTADO', "PREÇO MÁXIMO REVENDA", "ANO-MES"]])

    df_diff['ESTADO_MAX'] = df_gas_max_min.loc[idx_max, :]['ESTADO'].values
    df_diff['ESTADO_MIN'] = df_gas_max_min.loc[idx_min, :]['ESTADO'].values
    print(df_diff)

    # Verificando qual estado aparece mais vezes como o mais caro em termos de gasolina (com valores extremos)
    print(df_diff["ESTADO_MAX"].value_counts())

    # Refazendo com os valores médios de revenda

    df_diff_medio = pd.DataFrame()
    df_medio_max = df_gas_max_min_gpby['PREÇO MÉDIO REVENDA'].max()
    df_medio_min = df_gas_max_min_gpby['PREÇO MÉDIO REVENDA'].min()
    idx_medio_max = df_gas_max_min_gpby['PREÇO MÉDIO REVENDA'].idxmax()
    idx_medio_min = df_gas_max_min_gpby['PREÇO MÉDIO REVENDA'].idxmin()

    df_diff_medio["ABS_DIFF"] = df_medio_max - df_medio_min
    df_diff_medio["PERC_DIFF"] = (df_medio_max - df_medio_min)/df_medio_min * 100
    df_diff_medio["PMR_MIN"] = df_gas_max_min.loc[idx_medio_min, :]['PREÇO MÉDIO REVENDA'].values
    df_diff_medio["PMR_MAX"] = df_gas_max_min.loc[idx_medio_max, :]['PREÇO MÉDIO REVENDA'].values
    df_diff_medio["ESTADO_MIN"] = df_gas_max_min.loc[idx_medio_min, :]['ESTADO'].values
    df_diff_medio["ESTADO_MAX"] = df_gas_max_min.loc[idx_medio_max, :]['ESTADO'].values
    print(df_diff_medio)
    print(df_diff_medio['ESTADO_MAX'].value_counts())
    print(df_diff_medio['ESTADO_MIN'].value_counts())


analise_gasolina()
