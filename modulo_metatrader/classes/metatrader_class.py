import json
import os.path
from datetime import datetime, timedelta
from pathlib import Path

import MetaTrader5 as mt5
import pandas as pd

ohlc = Path.joinpath(Path.cwd().parent, 'ohlc')
ticks_dir = Path.joinpath(Path.cwd().parent, 'ticks')
class AsimoTrader():

    def __init__(self,metatrader_app_login=None, filepath=None, Login=None, password=None, server=None):
        if metatrader_app_login:
            if not mt5.initialize():
                print('Initialize() failed')
                mt5.shutdown()
        elif filepath:
            try:
                with open(filepath) as f:
                    credentials = json.load(f)

                self.login = credentials['loginJson']
                self.password = credentials['passwordJson']
                self.server = credentials['serverJson']
            except:
                print("Erro ao ler as credenciais")
                quit()
        elif Login or password or server:
            self.login = Login
            self.password = password
            self.server = server

            '''if(Login and password and server) == None:
                print("Erro ao ler as credenciais")
                quit()'''

            #Caso o mt5 não inicialize, quit()
            if not mt5.initialize(Login=self.login, password=self.password, server=self.server):
                print("initialize() failed, error code = ", mt5.last_error())
                mt5.shutdown()
                quit()


            # inicializando variaveis necessarias para as funções
        self.timeframe_dict = {
            # o quanto cada timeframe pode representar em dias? Ver estudos na função self.read_ohlc()
            'TIMEFRAME_M1': [mt5.TIMEFRAME_M1, 60],
            'TIMEFRAME_M2': [mt5.TIMEFRAME_M2, 120],
            'TIMEFRAME_M3': [mt5.TIMEFRAME_M3, 180],
            'TIMEFRAME_M4': [mt5.TIMEFRAME_M4, 240],
            'TIMEFRAME_M5': [mt5.TIMEFRAME_M5, 300],
            'TIMEFRAME_M6': [mt5.TIMEFRAME_M6, 360],
            'TIMEFRAME_M10': [mt5.TIMEFRAME_M10, 600],
            'TIMEFRAME_M12': [mt5.TIMEFRAME_M12, 720],
            'TIMEFRAME_M15': [mt5.TIMEFRAME_M15, 900],
            'TIMEFRAME_M20': [mt5.TIMEFRAME_M20, 1200],
            'TIMEFRAME_M30': [mt5.TIMEFRAME_M30, 1800],
            'TIMEFRAME_H1': [mt5.TIMEFRAME_H1, 3600],
            'TIMEFRAME_H2': [mt5.TIMEFRAME_H2, 7200],
            'TIMEFRAME_H3': [mt5.TIMEFRAME_H3, 10800],
            'TIMEFRAME_H4': [mt5.TIMEFRAME_H4, 14400],
            'TIMEFRAME_H6': [mt5.TIMEFRAME_H6, 21600],
            'TIMEFRAME_H8': [mt5.TIMEFRAME_H8, 28800],
            'TIMEFRAME_H12': [mt5.TIMEFRAME_H12, 43200],
            'TIMEFRAME_D1': [mt5.TIMEFRAME_D1, 86400],
            'TIMEFRAME_W1': [mt5.TIMEFRAME_W1, 604800],
            'TIMEFRAME_MN1': [mt5.TIMEFRAME_MN1, 2592000],
        }



        if not ohlc.exists():
            Path.mkdir(ohlc)
            for timeframe in self.timeframe_dict.keys():
                try:
                   Path.mkdir(Path.joinpath(ohlc, timeframe))
                except FileExistsError:
                   pass
        elif not ticks_dir.exists():
            Path.mkdir(ticks_dir)

    def update_ohlc(self, symbol, timeframe):
        initial_date = datetime(2012, 1, 1)
        final_date = datetime.now()

        if not Path.joinpath(ohlc, timeframe, f'{symbol}_{timeframe}.csv'):
            df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'tick_volume', 'spread', 'real_volume'])
        else:
            df = pd.read_csv(Path.joinpath(ohlc, timeframe, f'{symbol}_{timeframe}.csv'))
            df['time'] = pd.to_datetime(df['time'])
            if df['time'].max() < datetime.now() - timedelta(days=7):
                initial_date = df['time'].max()
            else:
                return

        timedelta_default = timedelta(days=self.timeframe_dict['timeframe'][1])
        final_date_aux = initial_date + timedelta_default
        timeframe_name = timeframe
        timeframe = self.timeframe_dict[timeframe][0]

        while True:
            data_aux = mt5.copy_rates_range(symbol, timeframe, initial_date, min(final_date_aux, final_date))
            df_aux = pd.DataFrame(data_aux)
            df_aux['time'] = pd.to_datetime(df_aux['time'], unit='s')
            df = pd.concat([df_aux, df], ignore_index=True)

            if final_date_aux > final_date:
                break

            initial_date = df_aux['time'].max()
            final_date_aux = initial_date + timedelta_default

        # Save df to file
        df.sort_values(by='time', ascending=False, inplace=True)
        #index=False evita que a cada vez que atualize seja gerada uma coluna unnamed_x que seria o índice para aquele update
        df.to_csv(Path.joinpath(ohlc, timeframe_name, f'{symbol}_{timeframe_name}.csv'),index=False)


    # Calculando apenas negocios efetivados, não todos.
    def update_ticks(self, symbol):
        initial_date = datetime(2012, 1, 1)
        final_date = datetime.now()

        if not Path.joinpath(ticks_dir, f'{symbol}_ticksrange.csv').exists():
            df = pd.DataFrame(columns=['time', 'bid', 'ask', 'last', 'volume', 'time_msc', 'flags', 'volume_real'])
        else:
            df = pd.read_csv(Path.joinpath(ticks_dir, f'{symbol}_ticksrange.csv'))
            df['time'] = pd.to_datetime(df['time'])
            if df['time'].max() < datetime.now() - timedelta(days=7):
                initial_date = df['time'].max()

        ticks_data = mt5.copy_ticks_range(symbol, initial_date, final_date, mt5.COPY_TICKS_TRADE)
        df_aux = pd.DataFrame(ticks_data)
        df_aux['time'] = pd.to_datetime(df_aux['time'], unit='s')
        df = pd.concat([df_aux, df], ignore_index=True)
        df['time'] = pd.to_datetime(df['time'])

        # Save df to file
        df.sort_values(by='time', ascending=False, inplace=True)
        df.to_csv(f'ticks\\{symbol}_ticksrange.csv', index=False)
        df.to_csv(Path.joinpath(ticks_dir, f'{symbol}_ticksrange.csv'), index=False)


                       
