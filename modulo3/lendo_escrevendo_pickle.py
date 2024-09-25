import pickle
from pathlib import Path


#Armazenamento de objetos serializados do python
def lendo_escrevendo_pickle():
    exports = Path.joinpath(Path.cwd(),'arquivos_mod3', 'exportacoes')
    pickles_folder = Path.joinpath(Path.cwd(), 'arquivos_mod3', 'pickles')
    if not pickles_folder.exists():
        Path.mkdir(pickles_folder)

    if not exports.exists():
        Path.mkdir(exports)

    #Salvando arquivo pickle
    minha_lista = [0,1,2]
    meu_dict = {"a":1, 'b':2}

    with open(Path.joinpath(pickles_folder, 'minha_lista.pickle'), 'wb') as f:
        pickle.dump(minha_lista, f)
    with open(Path.joinpath(pickles_folder, 'meu_dict.pickle'), 'wb') as f:
        pickle.dump(meu_dict, f)

    #Lendo arquivos pickle
    with open(Path.joinpath(pickles_folder, 'minha_lista.pickle'), 'rb') as f:
        minha_lista_lida = pickle.load(f)

    with open(Path.joinpath(pickles_folder, 'meu_dict.pickle'), 'rb') as f:
        meu_dict_lido = pickle.load(f)

    print(minha_lista_lida)
    print(meu_dict_lido)

    #Salvando a instância de uma classe com pickle
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def quem_sou_eu(self):
            print(f'Eu sou {self.nome} e tenho {self.idade} anos.')

    inst_john = Pessoa('John', 31)
    inst_john.quem_sou_eu()

    with open(Path.joinpath(pickles_folder, 'inst_john.pickle'), 'wb') as f:
        pickle.dump(inst_john, f)

    #Lendo a mesma instância
    with open(Path.joinpath(pickles_folder, 'inst_john.pickle'), 'rb') as f:
        inst_john_lida = pickle.load(f)

    inst_john_lida.quem_sou_eu()

lendo_escrevendo_pickle()