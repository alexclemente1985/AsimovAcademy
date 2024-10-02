from pathlib import Path
import random
import pandas as pd

def pedra_papel_tesoura():
    continuar = True
    regras_path = Path.joinpath(Path.cwd(), 'datasets', 'regras_jogo_ppt.csv')
    df_regras = pd.read_csv(regras_path, sep=';')
    placar = dict({"jogador":0,"pc":0})

    print("Bem vindo ao jogo PEDRA-PAPEL-TESOURA!\n")
    while continuar:
        escolha = input("Faça a sua escolha (pedra/papel/tesoura):\n")
        busca_regra = df_regras[df_regras["nome"] == escolha.strip().lower()]

        if len(busca_regra) == 0:
            print('Escolha inválida... tente novamente\n')
            continue
        else:
            escolha_pc = random.choice(list(range(0, 3, 1)))
            print("Computador escolheu: ", )
            print(df_regras[df_regras["valor"] == escolha_pc]["nome"].values[0], '\n')

            escolha_jogador = df_regras.loc[df_regras["nome"] == escolha.strip().lower()]

            vitoria = escolha_jogador["ganha"].values[0] == escolha_pc
            derrota = escolha_jogador["perde"].values[0] == escolha_pc

            if vitoria:
                print("Você ganhou! Parabéns!\n")
                placar["jogador"] += 1
            elif derrota:
                print("Você perdeu...\n")
                placar["pc"] += 1
            else:
                print("Eita! Empatou!\n")

            print("<<<<<Placar atual>>>>>")
            print(f"Jogador: {placar['jogador']} | Computador: {placar['pc']}\n")

            escolha_cont = input("Pressione qualquer tecla para continuar ou digite 'N' para sair:")

            match escolha_cont.upper():
                case 'N':
                    print("Jogo encerrado.")
                    break
                case other:
                    continue


pedra_papel_tesoura()
