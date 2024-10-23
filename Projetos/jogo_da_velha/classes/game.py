import random
from classes.player import Player
from typing import List


class Game:
    
    def __init__(self) -> None:
        self.game_match = 1
        self.players: List[Player] = []
        self.max_number_of_players = 0
        self.match_moves = 0
        self.max_match_moves = 9
        self.match_finished = False
        self.game_table: List[List] = list(list())
        
        self.game_symbols = ['X','O']
        self.available_symbols = self.game_symbols.copy()

        self.match_winner = ""
        self.last_match_winner = ""

        self.welcome()
    
    #Apresentação do jogo
    def welcome(self):
        print("\n<<<<< Bem vindo ao Jogo da Velha! >>>>>\n")

    #Inicialização padrão
    def initialize(self, number_of_players: int):
        self.set_number_of_players(number_of_players)
        self.add_player()
        self.set_initial_match_table()
        self.show_score()

        
            
    #Definição do número máximo de jogadores
    def set_number_of_players(self, number_of_players: int):
        self.max_number_of_players = number_of_players
    
    #Funções para players
    ##Símbolos disponíveis
    def remove_available_symbols(self, symbol: str):
        index = self.available_symbols.index(symbol)
        del self.available_symbols[index]
        
    def reset_available_symbols(self):
        self.available_symbols = self.game_symbols 
    
    ##Adição de jogadores (até 2)
    def add_player(self):
        for i in range(0,self.max_number_of_players):
            player_name = input(f"Informe o nome do jogador {i+1}: ")
            if len(self.available_symbols) > 1:
                while True:
                    player_symbol = input("Símbolo do jogador ('X' ou 'O'): ")

                    if (player_symbol.upper() != 'X') and (player_symbol.upper() != 'O'):
                        print("Símbolo não permitido. Tente novamente!\n")
                        continue
                    player_symbol = player_symbol.upper()
                    break
            else:
                player_symbol = self.available_symbols[0]
            
            player = Player(player_name,player_symbol, i)
            self.players.append(player)
            self.remove_available_symbols(player_symbol)

        if len(self.players) == 1:
            computer = Player("Computador",self.available_symbols[0], len(self.players))
            computer.set_computer_player()
            self.players.append(computer)
            self.remove_available_symbols(self.available_symbols[0])
                    
  
    #Funções da partida
            
    ##Preenchimento inicial da tabela do jogo
    def set_initial_match_table(self):
        self.game_table = [[f'{row+1}-{column+1}' for column in range(3)] for row in range(3)]
        
    
    ##Exibição da tabela do jogo
    def show_match_table(self, player: Player = None, is_start: bool = False):
        if (not self.match_finished) and (player):
            if is_start:
                print("\n<<<<< Tabela do jogo >>>>\n")            
        
        for line in self.game_table:
            line_value_list =[]
            for column in line:
                col_value = ""
                if column.strip() in self.game_symbols:
                    col_value = f" {column} "
                else:
                    col_value = column
                line_value_list.append(col_value)
            
            line_value = " | ".join(line_value_list)
            print(line_value)
           
        
    ##Atualização do número de jogadas
    def update_match_moves(self):
        self.match_moves+=1
    
    ##Realização da jogada
    def player_move(self, player: Player):
        if self.match_moves == 0: 
            self.update_match_moves() 
        if not player.isComputer:
            self.show_match_table(player, self.match_moves == 1)
        
        if(not self.match_finished):
            ###Rodada do computador
            if player.isComputer:
                while True:
                    comp_move = [random.choice(range(0,3)), random.choice(range(0,3))]

                    if self.game_table[comp_move[0]][comp_move[1]].strip() not in self.game_symbols:
                        self.game_table[comp_move[0]][comp_move[1]] = player.symbol
                        self.update_match_moves()
                        break
            ###Fim da rodada do computador    
            ###Rodada do jogador
            else:
                while True:
                    print(f"Escolha a posição da sua jogada, player {player.name}!\n")
                    input_row = input("Informe a linha da jogada: ")
                    input_column = input("Informe a coluna da jogada: ")

                    if (not input_row.isdigit()) or (not input_column.isdigit()):
                        print("Valores incorretos para linha e/ou coluna. Tente novamente!\n")
                        print(self.show_match_table(player))
                        continue
                    elif (not (int(input_row)-1) in range(0,3)) or (not (int(input_column)-1) in range(0,3)):
                        print("Valores de linha e/ou coluna fora dos limites da tabela do jogo. Tente novamente!\n")
                        print(self.show_match_table(player))
                        continue
                    else:
                        if self.game_table[int(input_row)-1][int(input_column)-1].strip() not in self.game_symbols:
                            self.game_table[int(input_row)-1][int(input_column)-1] = player.symbol
                            self.update_match_moves()
                        else:
                            print("Posição já previamente marcada na tabela. Tente novamente!\n")
                            print(self.show_match_table(player))
                            continue
                        
                    break
            ###Fim da rodada do jogador      
                
        self.verify_match()

        
    ##Início da partida
    def start_match(self):
        while True:
            if self.match_finished:
                self.show_match_table()
                print("Partida encerrada!\n")
                other_game = input("Deseja nova partida (digite 'n' ou 'N' para não, e qualquer tecla para sim)?\n")
                if other_game.upper() == 'N':
                    print("Encerrando o jogo... até a próxima!")
                    break
                else:
                    self.another_game()
            else:
                for player in self.players:
                    self.player_move(player)

    def win_handler(self, symbol: str, win_type: str, column: int = None, line: int = None):
        for p in self.players:
            if p.symbol == symbol:
                self.match_winner = p.name
                p.update_player_status()
            elif (win_type != 'n'):
                p.update_player_status(isLoss=True)                
            
        match win_type:
            case 'l':
                print(f"Partida acabou: linha {line} foi toda preenchida com {symbol}!")
            case 'c':
                print(f"Partida acabou: Coluna {column} foi toda preenchida com {symbol}!")
            case 'd':
                print(f"Partida acabou: Diagonal principal foi toda preenchida com {symbol}!")
            case 'rd':
                print(f"Partida acabou: Diagonal reversa foi toda preenchida com {symbol}!")
            case _:
                print("Partida acabou e deu Velha (empate)!")
                return
        
        print(f"Vencedor da partida nº {self.game_match}: {self.match_winner}")

    ##Verificando encerramento da partida            
    def verify_match(self):
        diagonal = list(str())
        reverse_diagonal = list(str())
        winner_symbol = ""
        #Criação de lista de tuplas com as colunas da tabela do jogo
        #transpose_game_table = [*zip(*self.game_table)]
        #Criação de matriz com as colunas da tabela do jogo (que agora são as linhas dessa matriz)
        game_table_columns = [list(i) for i in zip(*self.game_table)]

        for idx, column in enumerate(game_table_columns):
            if len(set(column)) == 1 and (not self.match_finished):
                self.match_finished = True
                winner_symbol = column[0]
                self.win_handler(winner_symbol, "c", idx+1)
                break
            

        for i, line in enumerate(self.game_table):
            if len(set(line)) == 1 and (not self.match_finished):
                self.match_finished = True
                winner_symbol = line[0]
                self.win_handler(winner_symbol, "l",None, i+1)
                break
            
            else:
                for j, c in enumerate(line):
                    if i == j:
                        diagonal.append("".join([str(i),str(j)]))
                        if i == 0:
                            reverse_diagonal.append("".join([str(i),str(j+2)]))
                        elif i == len(line) - 1:
                            reverse_diagonal.append("".join([str(i),str(j-2)]))
                        else:
                            reverse_diagonal.append("".join([str(i),str(j)]))

        #Verificação diagonal principal
        diagonal_set = set()
        for d in diagonal:
            diagonal_set.add(self.game_table[int(d[0])][int(d[1])])

        #Verificação diagonal reversa
        reverse_diag_set = set()
        for rd in reverse_diagonal:
            reverse_diag_set.add(self.game_table[int(rd[0])][int(rd[1])])
        
        if (len(diagonal_set) == 1) and (not self.match_finished):
            self.match_finished = True

            #Obtenção do valor do set (primeiro valor)
            for e in diagonal_set:
                winner_symbol = e
                break
            #Outros métodos:
            ##winner_symbol = next(iter(diagonal_set))

            self.win_handler(winner_symbol, "d")        
        
        if(len(reverse_diag_set) == 1) and (not self.match_finished):
            self.match_finished = True
            winner_symbol = next(iter(reverse_diag_set))
            self.win_handler(winner_symbol, "rd")
            
        if (self.match_moves > self.max_match_moves) and (not self.match_finished):
            self.match_finished = True
            self.win_handler(winner_symbol, "n")        
  
    #Acréscimo de partida de jogo
    def another_game(self):
        self.game_match += 1
        self.match_finished = False
        self.match_moves = 0
        self.match_winner = ""
        self.set_initial_match_table()
        self.show_score()

    #Exibição do score por jogador (função __str__ de Player)
    def show_score(self):
        for player in self.players:
            print(player)   
    
