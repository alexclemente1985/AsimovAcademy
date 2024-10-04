from classes.game import Game

class Player(Game):
    def __init__(self, name: str, wins: int, losses: int) -> None:
        self.nome = name
        self.wins = wins
        self.losses = losses
        self.max_winning_streak = 0
        self.max_consecutive_losses = 0

    
    
    def __str__(self) -> str:
        return f"Jogador: {self.name} | Vitórias: {self.wins} | Recorde de vitórias consecutivas: {self.max_winning_streak} | Derrotas: {self.losses} | Recorde de derrotas consecutivas: {self.max_consecutive_losses} "