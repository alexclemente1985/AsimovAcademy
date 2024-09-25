import json
from pathlib import Path
import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

def lendo_escrevendo_json():
    json_file = Path.joinpath(Path.cwd(), 'arquivos_mod3', 'assinantes.json')

    #Leitura do arquivo json e convertendo para dicionário
    with open(json_file) as json_data:
        #json.loads() -> quando for ler um formato string que represente uma saída json (leitura total de uma só vez)
        data = json.load(json_data)

    #Criação de dado json, evitando ascii (não reconhece caracteres como "ç" e "~") e com indentação múltipla de 2 (tabs)
    new_json = json.dumps(data, ensure_ascii=False, indent=2)
    print(new_json)
    print(type(new_json))

    #Escrevendo arquivos json
    exports = Path.joinpath(Path.cwd(),'arquivos_mod3', 'exportacoes')
    if not exports.exists():
        Path.mkdir(exports)

    with open(Path.joinpath(exports, 'assinantes_copia.json'), mode='w') as copy:
        json.dump(new_json, copy, indent=2, ensure_ascii=False)

lendo_escrevendo_json()