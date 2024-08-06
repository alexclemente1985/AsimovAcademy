import csv
from typing import TextIO


def database_dictionary(database):
    dados = list(dict())

    try:
        for row in database:
            row_split = row[0].split(";")
            dados.append(
                {"index": row_split[0], "carro": row_split[1], "diaria":row_split[2], "disponivel":row_split[3]}
            )

        for d in dados:
            print("dados: ", d)
    except Exception as e:
        print("Deu ruim...", e)
