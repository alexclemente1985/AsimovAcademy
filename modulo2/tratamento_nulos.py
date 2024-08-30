import numpy as np
import pandas as pd


def tratamento_nulos():
    df = pd.DataFrame({'A': [1,2,np.nan],
                       'B': [5, np.nan, np.nan],
                       'C': [1,2,3]})

    print(df)

    #Removendo nulos (somente registro sem nenhum dado nulo será mantido)
    ##Corte nas linhas
    df_sem_nulos_linhas = df.dropna() #df.dropna(axis=0)
    ##Corte nas colunas
    df_sem_nulos_cols = df.dropna(axis=1)
    print(df_sem_nulos_linhas)
    print(df_sem_nulos_cols)

    #Thresh -> informa limite de tolerância de nulos
    df_thresh = df.dropna(axis=1, thresh=2)
    print(df_thresh)

    #Preenchimento dos dados nulos
    df_preenchido = df.fillna("NULO!")
    print(df_preenchido)

    #Preenchimento com valores médios da linha
    df_preenchido_A = df.fillna(value=df["A"].mean())
    print(df_preenchido_A)

    #Preenche nulos com o último valor observado na coluna(ótimo para séries temporais em dados financeiros)
    df_preenchido_ultimo_valor = df.ffill()
    print(df_preenchido_ultimo_valor)

    #Pega última info da coluna e preenche as anteriores (não vai funcionar nesse caso)
    df_preenchido_ultimo_valor_bkfill = df.bfill()
    print(df_preenchido_ultimo_valor_bkfill)

tratamento_nulos()