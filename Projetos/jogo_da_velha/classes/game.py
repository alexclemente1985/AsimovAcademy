class Game:
    def __init__(self) -> None:
        self.round = 0
        self.players = []
    
    def welcome(self):
        print("Bem vindo ao Jogo da Velha")
    
    def add_player(self):
        pass
    def remove_player(self):
        pass
    
    def another_game(self):
        self.round += 1

    def show_score(self):
        pass
    
    def reset_game(self):
        self.round = 0
        self.players = []
