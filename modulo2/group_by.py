import pandas as pd


def group_by():
    data = {'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'],
            'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
            'Venda': [200, 220, 340, 124, 443, 350]}

    df = pd.DataFrame(data)
    print(df)

    # Agrupamentos em dataframes
    ## Verificação de vendas por classes
    df_group_classes = df.groupby("Classe")
    df_classe_vendas = df.drop(['Nome'], axis=1)
    df_group_classes_vendas = df_classe_vendas.groupby('Classe')

    ##Somatório de vendas por classe:
    print(df_group_classes_vendas.sum())

    ##Média das vendas por classe:
    print(df_group_classes_vendas.mean())

    ##Piores vendas de cada classe
    ###Jeito errado: vai trazer o mínimo de cada coluna, desvinculando o Nome e Venda
    print(df_group_classes.min())

    ###Jeito certo: usando apply e lambda no groupby
    print(df_group_classes.apply(lambda g: g[g["Venda"] == g["Venda"].min()], include_groups=False))

    ##Melhores vendas de cada classe
    print(df_group_classes.apply(lambda g: g[g["Venda"] == g["Venda"].max()], include_groups=False))

    #Copiando dataframes -> evita alterações no original por conta do ponteiro ao endereço
    df2 = df.copy()
    df2["Venda"] = [150,432,190,230,410,155]
    print(df2)
    print(df)

    #Concatenação de dataframes
    df3 = pd.concat([df, df2])

    print("\n")
    print(df3)

    #Agrupamento do df3 para simular vários períodos de vendas (agrupamento multinível)
    df3_groupby_classe_nome = df3.groupby(['Classe','Nome'])
    print(df3_groupby_classe_nome.sum())

group_by()
