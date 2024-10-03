class Animal():
    def __init__(self, animal: str) -> None:
        print(f"{animal} criado")
        self.animal = animal
    def quem_sou_eu(self):
        print("Eu sou um animal")
    def correr(self):
        print(f"{self.animal} correndo")

    def __str__(self, nome, raca) -> str:
        return f"O que vc quer saber sobre o animal {self.animal} chamado {nome}? Parece que é da raça {raca}"