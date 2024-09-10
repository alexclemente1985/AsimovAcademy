from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from tvDatafeed import TvDatafeed


# from tvDatafeed import TvDatafeed
#NOTA: por não ser lib oficial, está apresentando problemas diversos (e não realiza login)

def tvdata_feed():
    username = 'alexclemente1985'
    pass_path = Path.joinpath(Path.cwd().parent, 'passwords')
    print(pass_path)
    password = open(Path.joinpath(pass_path, 'pass.txt')).read()

    print(username, password)
    try:
        tv = TvDatafeed(username, password)
        print('tv ', tv.token)

        tv.search_symbol('PETR4','BMFBOVESPA')
        petros = tv.get_hist(symbol='PETR4',exchange='BMFBOVESPA')
        print('teste petros (PETR4): \n',petros)
        # if tv.token == 'unauthorized_user_token':
        #   tv = TvDatafeed(auto_login=False)
    except Exception as e:
        print(f"Erro ao tentar login: {e}")


tvdata_feed()
