def display_menu_opcoes(opcoes):
    op_array = list()

    for op in opcoes.keys():
        op_array.append(" - ".join([f"{op}", opcoes[op]]))

    opcoes_menu = " | ".join(op_array)

    print(opcoes_menu)

def menu_locadora():
    print("Bem vindo à locadora de carros!")
    print("========")
    print("O que deseja fazer?")

    opcoes = {0: "Mostrar portfólio", 1: "Alugar um carro", 2: "Devolver um carro"}

    try:
        escolha = int(input(display_menu_opcoes(opcoes)))
        return escolha
    except:
        #implementar o loop
        print("Escolha inválida... tente novamente")
