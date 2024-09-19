from datetime import datetime, timedelta
from pathlib import Path
from matplotlib import pyplot
import pandas as pd


def series_temp_manip():
    data_path = Path.joinpath(Path.cwd(), 'dataset', 'petr4_ticks.csv')
    df_intra = pd.read_csv(data_path, sep=';', decimal=',')


    df_intra.rename(columns={"time": "datetime"}, inplace=True)
    df_intra.set_index("datetime", inplace=True)

    print(df_intra)
    df_intra.index = pd.to_datetime(df_intra.index)

    print(df_intra.index.date)
    print(df_intra.index.weekday)
    print(df_intra[df_intra.index.date == (datetime.today() - timedelta(days=20)).date()])

    #Filtro em determinada janela temporal
    d0 = datetime(2024,8,17)
    d1 = datetime(2024,9,1)
    #print("Filtro d0 e d1")
    #print(df_intra[(datetime(df_intra.index.year,df_intra.index.month, df_intra.index.day) > d0)])
    #print(df_intra[(df_intra.index > d0) & (df_intra.index < d1)])

    #Rolling -> bom para médias móveis -> suaviza o gráfico
    df_slice = df_intra[df_intra.index.date == (datetime.today() - timedelta(days=20)).date()]
    df_slice["last"].plot()
    pyplot.show()
    pyplot.close()

    #window: agrupamento de 5 em 5 (no caso) (problema com o índice e a base de dados adaptada)
    df_slice["rm5"] = df_slice.rolling(window=5)["last"].mean().head(50)

    df_slice["rm5"].plot()
    df_slice["last"].plot()
    pyplot.show()



series_temp_manip()
