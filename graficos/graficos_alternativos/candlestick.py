import plotly.graph_objects as go
import pandas as pd
from pathlib import Path


def candlestick():
    database = Path.joinpath(Path.cwd(),'datasets','finance-charts-apple.csv')
    df = pd.read_csv(database)
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                         open=df['AAPL.Open'], high=df['AAPL.High'],
                                         low=df['AAPL.Low'], close=df['AAPL.Close'])
                          ])

    fig.update_layout(height=700)
    fig.show()
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()


candlestick()
