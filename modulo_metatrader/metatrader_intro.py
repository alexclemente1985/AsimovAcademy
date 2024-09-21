from datetime import datetime
from pathlib import Path

import MetaTrader5 as mt5
import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def metatrader_intro():
    credentials = Path.joinpath(Path.cwd(),'credentials','credentials.json')
    #Comandos básicos
    ## Acesso à base (caso não acesse o aplicativo logado)
    with open(credentials) as f:
        data = json.load(f)
    print(data)

    if not mt5.initialize():
        print('Initialize() failed')
        mt5.shutdown()
    print(mt5.account_info())

    print(mt5.symbols_total())

    #Informações do ativo escolhido (na forma de dicionário)
    print(mt5.symbol_info('IBOV11')._asdict())

    #Não precisou pq o aplicativo já logou e o python já se conecta nele logado
    '''
    account = mt5.login(Login=data['loginJson'], password=data['passwordJson'], Server=['serverJson'])
    if account:
        print('Logado com sucesso na conta ', account['login'])
    else:
        print(f'Falha no login da conta: {mt5.last_error()}')'''



    '''if not mt5.initialize(Login=data['loginJson'], password=data['passwordJson'], server=data['serverJson']):
        print("initialize() failed, error code = ", mt5.last_error(), '\n',mt5.account_info())
        mt5.shutdown()
        quit()'''


    #Estrutura de um OHLC -> Open/High/Low/Close
    ## Relacionado aos gráficos de vela (candlestick)

    '''
        copy_rates_range(
           symbol, // nome do ativo
           timeframe, // timeframes do MT5 (janelas de tempo)
           date_from, // data inicial
           date_to, // data final 
        )
    '''

    data = mt5.copy_rates_range("PETR4", mt5.TIMEFRAME_W1, datetime(2022, 1,1), datetime.now())

    df = pd.DataFrame(data)
    print(df.head())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df.head())

    #gráfico

    fig = px.line(df, x=df['time'], y=df['close'])


    fig.show()

    fig.update_xaxes(dtick='M8', tickformat='%b/%Y')
    fig.show()

    #Gráficos de vela
    fig2 = go.Figure(data=[go.Candlestick(
        x=df['time'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    fig2.show()

    ## NOTAS DA AULA DE GRÁFICOS DE VELA
    '''
        Wick (pavio) -> representa o maior preço dentro do período de tempo
        Tail (cauda) -> representa o menor preço dentro do período de tempo
        Wick e Tail são consideradas Shadows (Upper Shadow e Lower Shadow, respect)
        Vela verde -> Preço subiu no período de tempo
        Vela vermelha -> Preço caiu no período de tempo
        
        Open -> Valor de abertura do dia
        Close -> Valor de encerramento do dia
        
        Nota: Open e close são invertidos na comparação entre velas vermelhas e verdes
        --> Verde: Open embaixo e Close em cima
        --> Vermelho: Open em cima e Close embaixo
        
        Real Body -> "Corpo" da vela dentro do timeframe
        --> Representa a expectativa do mercado
        --> Dicas:
        ---> Interpretar o swing da vela e não somente o output (se positivo ou negativo)
        ---> Tails são informações valiosas do que ocorreu
        ----> Ex: Bearish Candle com pequeno Real Body e grande Tail (Bottom/Lower Shadow):
        -----> Significa que o o preço caiu muito naquele timeframe (dia, semana, etc), mas mercado tende a subir
        -----> Real Body pequeno com Tail grande representa comeback (tendência de inversão, no caso para cima)
        
        Doji Candles -> Velas de indecisão: o preço não variou no tempo de maneira significativa
    '''

    #Tick Data

    '''
        bids -> solicitações de venda
        asks -> solicitações de compra
        spread -> diferença entre os bids e asks
    '''

    data_tick = mt5.copy_ticks_range("PETR4", datetime(2020,1,1), datetime.now(), mt5.COPY_TICKS_ALL)

    df_ticks = pd.DataFrame(data_tick[:5000])
    print(df_ticks.head())

    data_tick_trade = mt5.copy_ticks_range("PETR4", datetime(2020,1,1), datetime.now(), mt5.COPY_TICKS_TRADE)

    df_tick_trade = pd.DataFrame(data_tick_trade[:5000])
    print(df_tick_trade.head())



metatrader_intro()