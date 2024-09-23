from datetime import datetime
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


from modulo_metatrader.classes.metatrader_class import AsimoTrader


def mtd_teste_class():
    #Para o caso de não haver conexão automática com metatrader logado (colocar credenciais no json)
    file_path = Path.joinpath(Path.cwd(),'credentials','credentials.json')
    trader = AsimoTrader(filepath=file_path)

    trader.update_ohlc(symbol="PETR4", timeframe='TIMEFRAME_M1')
    df = trader.read_ohlc(symbol='PETR4', timeframe='TIMEFRAME_M1', initial_date=datetime(2022,1,1))

    print(df.head())

    print(df['time'].min())

    #Gráfico de linha
    fig = px.line(df, x=df['time'], y=df['close'])
    #espaçamento de 8 meses e formato "Mês abrevidado/ ano"
    fig.update_xaxes(dtick="M8", tickformat="%b/%Y")
    fig.show()

    #Gráfico Candlestick
    fig = go.Figure(data=go.Candlestick(x=df['time'],
                                        open=df['open'],
                                        close=df['close'],
                                        low=df['low'],
                                        high=df['high']))

    fig.update_xaxes(dtick="M8", tickformat="%b/%Y")

    fig.show()

    #Atualizando os ticks com update_ticks
    trader.update_ticks(symbol="PETR4")

mtd_teste_class()