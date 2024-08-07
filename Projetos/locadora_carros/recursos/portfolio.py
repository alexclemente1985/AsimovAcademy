from typing import List, Dict

from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora


def display_veiculos(veiculo: Dict):
    print(f"[{veiculo['index']}] {veiculo['carro']} - R$ {veiculo['diaria']} /dia")

def portfolio(port: List[Dict]):
    print("\nLista de todos os veículos da locadora: \n")
    for v in port:
        display_veiculos(v)

    return menu_locadora()

