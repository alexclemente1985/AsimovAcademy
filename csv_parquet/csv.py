import time
import pandas as pd
from pathlib import Path


def csv():

    #Leitura
    t0 = time.time()
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    # df = pd.read_csv(Path.joinpath(datasets, 'petr4_ticks.csv', sep=';', decimal=',')
    t1 = time.time()
    print(f"Tempo para leitura com pandas.read_csv(): {t1 - t0}")

    #Escrita
    t0 = time.time()
    # df = pd.to_csv(Path.joinpath(datasets, 'petr4_ticks.csv', sep=';', decimal=',')
    t1 = time.time()
    print(f"Tempo para leitura com pandas.to_csv(): {t1 - t0}")


csv()
