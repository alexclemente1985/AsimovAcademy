import csv

# from Projetos.locadora_carros.recursos.database_dictionary import database_dictionary
# from Projetos.locadora_carros.recursos.menu_locadora import menu_locadora

import os
from pathlib import Path
import csv

from AsimovAcademy.Projetos.locadora_carros.recursos.database_dictionary import database_dictionary
from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora
from AsimovAcademy.Projetos.locadora_carros.recursos.portfolio import portfolio


def locadora():
    try:
        db_path = Path(__file__).parent / "recursos/db/carros.csv"

        print("db path: ", db_path)
        database = csv.reader(open(db_path))
        dados = database_dictionary(database)
        print("dados: ", dados)
        escolha = menu_locadora()

        while escolha in [0, 1, 2]:
            match escolha:
                case 0:
                    escolha = portfolio(dados)
                case 1:
                    continue
                case 2:
                    continue

        else:
            print("Finalizando o programa")



    except Exception as e:
        print("Erro na execução do programa: ", e)


if __name__ == '__main__':
    locadora()
