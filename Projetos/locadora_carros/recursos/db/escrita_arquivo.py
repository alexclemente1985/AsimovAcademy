from typing import List, Dict


def escrita_arquivo(caminho, veiculos: List[Dict]):
    try:
        with open(caminho, 'w') as arquivo:
            for veiculo in veiculos:
                index = veiculo['index']
                nome = veiculo['nome']
                diaria = veiculo['diaria']
                disponivel = veiculo['disponivel']
                tempo = veiculo['tempo']

                arquivo.write(f"{index};{nome};{diaria};{disponivel};{tempo}\n")
    except Exception as e:
        print("Erro na escrita do arquivo: ", e)
    else:
        print(">>> Alterações salvas com sucesso <<<")
