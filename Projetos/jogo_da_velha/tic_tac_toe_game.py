from classes.game import Game


def tic_tac_toe_game():
    game = Game()

    while True:
        game_type = input("Escolha o tipo de jogo -> 1 Jogador (1) | 2 Jogadores (2): ")

        if game_type == "1" or game_type == "2":
            game.initialize(int(game_type))
            game.start_match()
            
            break
        else:
            print("Opção incorreta. Tente novamente.")
            continue


tic_tac_toe_game()