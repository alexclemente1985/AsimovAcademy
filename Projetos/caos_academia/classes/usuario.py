import random
from classes.academia import Academia

class Usuario(Academia):
    def __init__(self, tipo: int, academia: Academia) -> None:
        self.tipo = tipo
        self.academia = academia
        self.peso = 0


    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halter(self.peso)
    
    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        #Usuário organizado
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        #Usuário desorganizado
        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        
        self.peso = 0