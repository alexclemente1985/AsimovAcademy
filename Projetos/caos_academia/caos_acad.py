import random
from classes.academia import Academia
from classes.usuario import Usuario
import seaborn as sns
import matplotlib.pyplot as plt

def caos_acad():
    academia = Academia()
    usuarios = [Usuario(1, academia) for i in range(10)]
    usuarios += [Usuario(2, academia) for i in range(1)]

    random.shuffle(usuarios)

    list_chaos = []

    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
        list_chaos += [academia.calcular_caos()]
    
    print(academia.porta_halteres)
    print(list_chaos)
    
    print(f"Relação do CAOS na academia, com {len([user for user in usuarios if user.tipo == 2])} usuário(s) caóticos: {list_chaos[-1]}")
    sns.displot(list_chaos)
    
    plt.show()
    

caos_acad()