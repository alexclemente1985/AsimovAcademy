#Uso do SQL Lite
import sqlite3
from pathlib import Path

import pandas as pd
def sql():
    #Criando conexão com banco de dados SQLITE
    database = Path.joinpath(Path.cwd(),"databases","web.db")
    print(database)
    conn = sqlite3.connect(database)
    bd_data = Path.joinpath(Path.cwd(),"datasets","bd_data.csv")
    df_data = pd.read_csv(bd_data, index_col=0)
    df_data.index.name = "index_name"
    print(df_data)

    df_data.to_sql('data',conn, index_label='index_name')

sql()