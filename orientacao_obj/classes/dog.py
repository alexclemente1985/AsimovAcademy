from classes.herancas.animal import Animal


class Dog(Animal):
    def __init__(self, nome: str, idade: int = 10, raca: str = "Indefinida") :
        Animal.__init__(self, "Cachorro")
        self.nome = nome
        self.idade = idade
        self.raca = raca
    
    def envelhecer(self):
        print(f"O cãozinho {self.nome} está envelhecendo...")
        self.idade += 1
    
    def quem_sou_eu(self):
        print("Eu sou um cachorro")

    def __str__(self) -> str:
        return super().__str__(self.nome, self.raca)