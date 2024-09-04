from pathlib import Path

import pandas as pd
#Para o caso de falhas de leitura html no Mac
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def entrada_saida():
    # Parâmetros
    ##Index_col = permite definir uma coluna como índice
    ##Parse_dates = verifica quais campos podem ser do tipo data e formata da melhor maneira (True | False)
    df = pd.read_csv(Path.joinpath(Path.cwd().parent, "datasets", "exemplo.csv"), sep=",", decimal=".")

    print(df)
    # Para verificar se todos os dados foram considerados como do tipo float para o caso
    print(df.info())

    # Para exportar o conjunto de dados
    df.to_csv(Path.joinpath(Path.cwd().parent, "datasets", "exports", "exemplo_exp.csv"), sep=";", decimal=",")

    # Leitura e escrita de arquivo excel
    df.to_excel(Path.joinpath(Path.cwd().parent, "datasets", "exports", "exemplo_exp.xlsx"), sheet_name="Planilha1")
    df_excel = pd.read_excel(Path.joinpath(Path.cwd().parent, "datasets", "exports", "exemplo_exp.xlsx"),
                             sheet_name="Planilha1")
    print(df_excel)

    # Leitura de HTML
    df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
    print(df_html)


entrada_saida()
