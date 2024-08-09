from typing import List, Dict


def leitura_arquivo(path):
    try:
        veiculos: List[Dict] = list()
        with open(path, 'r') as arquivo:

            for linha in arquivo:
                index, nome, diaria, disponivel, tempo = linha.strip().split(";")
                veiculo = {
                    "index": index,
                    "nome": nome,
                    "diaria":diaria,
                    "disponivel":disponivel,
                    "tempo": tempo
                }
                veiculos.append(veiculo)
    except FileNotFoundError as e:
        print("Erro de arquivo não encontrado: ", e)
    except Exception as e:
        print("Erro na leitura do arquivo: ", e)
    else:
        print(">>> Dados carregados com sucesso. <<<")
        return veiculos

    return []

