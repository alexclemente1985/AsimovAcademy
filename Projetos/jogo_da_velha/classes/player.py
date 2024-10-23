

class Player():
    def __init__(self, name: str, symbol: str, id: int) -> None:
        self.id = id
        self.name = name
        self.wins = 0
        self.losses = 0
        self.winning_streak = 0
        self.consecutive_losses = 0
        self.max_winning_streak = 0
        self.max_consecutive_losses = 0
        self.symbol = symbol
        self.isComputer = False        

    def set_computer_player(self):
        self.isComputer = True
    
    def update_player_status(self, isLoss: bool = False):
        if isLoss:
            self.losses += 1
            self.consecutive_losses += 1

            if self.winning_streak != 0:
                self.winning_streak = 0
            
            # - 1 pois tem que descontar a primeira derrota da sequência (pois não é consecutiva a nenhuma outra)
            if self.consecutive_losses-1 > self.max_consecutive_losses:
                self.max_consecutive_losses = self.consecutive_losses - 1
        else:
            self.wins += 1
            self.winning_streak += 1

            if self.consecutive_losses != 0:
                self.consecutive_losses = 0

            if self.winning_streak-1 > self.max_winning_streak:
                self.max_winning_streak = self.winning_streak - 1

    
    def __str__(self) -> str:
        return f"Jogador: {self.name} | Vitórias: {self.wins} | Recorde de vitórias consecutivas: {self.max_winning_streak} | Derrotas: {self.losses} | Recorde de derrotas consecutivas: {self.max_consecutive_losses} "