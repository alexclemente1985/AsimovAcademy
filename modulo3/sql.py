# Uso do SQL Lite
import os
import sqlite3
from pathlib import Path

import pandas as pd


def sql():
    # Criando conexão com banco de dados SQLITE
    path = Path.joinpath(Path.cwd(), "databases")
    # Criando pasta database caso não exista
    if not path.exists():
        Path.mkdir(path, exist_ok=True)

    database = Path.joinpath(Path.cwd(), "databases", "web.db")
    print(database)
    conn = sqlite3.connect(database)
    bd_data = Path.joinpath(Path.cwd(), "datasets", "bd_data.csv")
    df_data = pd.read_csv(bd_data, index_col=0)
    df_data.index.name = "index_name"
    print(df_data)

    df_data.to_sql('data', conn, index_label='index_name', if_exists='replace')

    # Criação do cursor para alterar a base de dados
    c = conn.cursor()
    # c.execute('CREATE TABLE IF NOT EXISTS products (product_id, product_name, price)')
    # c.execute('CREATE TABLE products (product_id, product_name, price)')
    # conn.commit()

    c.execute('DROP TABLE products')
    # c.execute('DROP TABLE data')
    conn.commit()

    c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, '
              '[price] INTEGER)')
    ##c.execute('CREATE TABLE IF NOT EXISTS products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, '
    #          '[price] INTEGER)')

    # INSERT
    c.execute('''INSERT INTO products (product_id, product_name, price)
        VALUES
        (1, 'Computer', 800),
        (2, 'Printer', 200),
        (3, 'Tablet', 300)
    ''')
    conn.commit()

    # df_data2 = df_data.iloc[::-2]
    # df_data2.to_sql('data', conn, if_exists='append')

    # SELECT
    c.execute('''SELECT * FROM data''')
    print(c.fetchone())
    df_fetchall = pd.DataFrame(c.fetchall())
    print('---')
    print(df_fetchall)

    c.execute("SELECT * FROM data WHERE A > 200")
    df_fetchall = pd.DataFrame(c.fetchall())
    print('---')
    print(df_fetchall)

    c.execute("SELECT * FROM data WHERE A > 200 AND B > 100")
    df_fetchall = pd.DataFrame(c.fetchall())
    print('---')
    print(df_fetchall)

    c.execute("SELECT A,B,C FROM data WHERE A > 200 AND B > 100")
    df_fetchall = pd.DataFrame(c.fetchall())
    print('--- fechall A, B, C')
    print(df_fetchall)

    query = "SELECT * FROM data"
    query2 = "SELECT A,B,C FROM data WHERE A > 200 AND B > 100"
    df_query = pd.read_sql(query, con=conn, index_col='index_name')
    df_query2 = pd.read_sql(query2, con=conn)

    print("query 1 ------------")
    print(df_query)
    print("query 2 ------------")
    print(df_query2)

    #UPDATE E DELETE
    c.execute("UPDATE data SET A=298, B=300 WHERE index_name='b'")
    conn.commit()
    print(pd.read_sql(query2, con=conn))
    c.execute("DELETE FROM data WHERE index_name=1")
    print(pd.read_sql(query, con=conn, index_col='index_name'))



sql()
