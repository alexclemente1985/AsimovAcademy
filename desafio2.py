import datetime
import shutil
from pathlib import Path


def desafio2():
    pasta_raiz = Path(__file__).parent
    pasta_a_organizar = pasta_raiz / 'arquivos_desafio2'
    pasta_organizada = pasta_raiz / 'arquivos_desafio2_org'
    pasta_bkps = pasta_raiz / 'arquivos_desafio2_bkps'

    if pasta_organizada.exists():
        shutil.rmtree(pasta_organizada)

    pasta_organizada.mkdir()

    if not pasta_bkps.exists():
        pasta_bkps.mkdir()

    for arq in pasta_a_organizar.glob('**/*'):
        if arq.is_file():
            pasta_org_ext = pasta_organizada / arq.suffix.replace('.','')

            if not pasta_org_ext.exists():
                pasta_org_ext.mkdir()

            shutil.copy(arq, pasta_org_ext)

    nome_bkp = datetime.datetime.now().strftime('%Y_%m_%d')
    shutil.make_archive(pasta_bkps / nome_bkp, 'zip', pasta_organizada)

desafio2()