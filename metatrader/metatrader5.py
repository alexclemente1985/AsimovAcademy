from pathlib import Path

import MetaTrader5 as mt5
from datetime import datetime, timedelta
import pandas as pd

def metatrader5():

    def buy_or_sell(flag):
        '''

        https://www.mql5.com/en/forum/75268 para explicação sobre MetaTrader flags
        '''

        if(flag & 32) and (flag & 64):
            return 'both'
        elif flag & 32:
            return 'buy'
        elif flag & 64:
            return 'sell'


    if not mt5.initialize():
        print('Initialize() failed')
        mt5.shutdown()

    symbols = mt5.symbols_get()
    print('Symbols: \n', symbols)

    #Dados de ticker
    petr4 = mt5.symbol_info('PETR4')
    print('PETR4 \n',petr4)

    #Dados de Ticks -> cada microvariação de preço no mercado
    ticker = 'PETR4'
    t0 = datetime.today() - timedelta(days=220)
    t1 = datetime.today()
    #COPY_TICKS_TRADE - apenas negociações
    ticks_range = mt5.copy_ticks_range(ticker, t0, t1, mt5.COPY_TICKS_TRADE)
    df_ticks = pd.DataFrame(ticks_range)
    print(df_ticks)

    df_ticks.set_index('time', inplace=True)
    df_ticks.index = pd.to_datetime(df_ticks.index, utc=True, unit='s')
    print('----------------------------------------------------------------------------')
    print(df_ticks)

    df_ticks['flags'] = df_ticks['flags'].apply(buy_or_sell)

    exports = Path.joinpath(Path.cwd(), 'exports')
    df_ticks.to_csv(Path.joinpath(exports,'petr4_ticks.csv'), sep=';', decimal=',')


metatrader5()