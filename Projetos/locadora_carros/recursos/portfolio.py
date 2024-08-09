from typing import List, Dict

from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora


def display_veiculos(veiculo: Dict):
    print(f"[{veiculo['index']}] {veiculo['nome']} "
          f"- R$ {veiculo['diaria']} /dia "
          f"{' - Aluguel: '+str(veiculo['tempo'])+' dias' if int(veiculo['tempo']) > 0 else ''}")

def portfolio(tipo: int, port: List[Dict]):
    match tipo:
        case 0:
            portfolio_total(port)
        case 1:
            portfolio_disponivel(port)
        case 2:
            portfolio_devolucao(port)

def portfolio_disponivel(port: List[Dict]):
    print("\n[ ALUGAR ] Dê uma olhada em nosso portfólio.\n")

    for v in port:
        if v["disponivel"] == "True":
            display_veiculos(v)

def portfolio_devolucao(port: List[Dict]):
    print("\n[ DEVOLVER ] Veículos que deverão ser devolvidos.\n")
    for v in port:
        if v["disponivel"] == "False":
            display_veiculos(v)


def portfolio_total(port: List[Dict]):
    print("\nLista de todos os veículos da locadora: \n")
    for v in port:
        display_veiculos(v)



