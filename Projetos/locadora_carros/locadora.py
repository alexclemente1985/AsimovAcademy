import csv

from Projetos.locadora_carros.recursos.database_dictionary import database_dictionary
from Projetos.locadora_carros.recursos.menu_locadora import menu_locadora
import os
from pathlib import Path
import csv

def locadora():
    try:
        db_path = Path(__file__).parent/"recursos/db/carros.csv"

        print("db path: ", db_path)
        database = csv.reader(open(db_path))
        database_dictionary(database)
        escolha = menu_locadora()

    except Exception as e:
        print("Erro na execução do programa: ", e)


if __name__ == '__main__':
    locadora()
