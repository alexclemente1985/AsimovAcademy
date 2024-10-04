class Academia:
    def __init__(self) -> None:
        self.halteres = [i for i in range(10,36) if i%2==0]
        print(f"Lista de halteres: {self.halteres}")
        self.porta_halteres = {}
        self.reiniciar_o_dia()
    
    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}
        print(f"Porta-halteres reinicializado: {self.porta_halteres}")
    
    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def listar_espacos(self):
        return [i for i,j in self.porta_halteres.items() if j == 0 ]
    
    def pegar_halter(self, peso):
        #index(peso) permite pegar o índice que representa a posição no porta-halteres para o peso informado
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]

        #"Pegou" o halter
        self.porta_halteres[key_halt] = 0
        return peso
    
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso
    
    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i!=j]
        #Retorna a razão do caos na academia (1 = Caos total | 0 = Organização total)
        return len(num_caos)/len(self.porta_halteres)
