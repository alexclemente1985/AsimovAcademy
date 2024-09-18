import plotly.graph_objects as go
import numpy as np


def boxplots():
    np.random.seed(1)

    y0 = np.random.randn(50) - 1
    y1 = np.random.randn(50) + 1

    fig = go.Figure()
    fig.add_trace(go.Box(y=y0))
    fig.add_trace(go.Box(y=y1))

    fig.update_layout(height=600)
    fig.show()

    # Plotando horizontalmente

    x0 = np.random.randn(50)
    x1 = np.random.randn(50) + 2  # shift mean

    fig = go.Figure()

    # Para plotar horizontalmente, basta substituir x por y
    fig.add_trace(go.Box(x=x0))
    fig.add_trace(go.Box(x=x1))

    fig.show()

    # Agrupando boxes
    x = ['dia 1', 'dia 1', 'dia 1', 'dia 1', 'dia 1', 'dia 1',
         'dia 2', 'dia 2', 'dia 2', 'dia 2', 'dia 2', 'dia 2']

    fig = go.Figure()

    fig.add_trace(go.Box(
        y=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
        x=x,
        name='couve',
        marker_color='#3AF970'
    ))
    fig.add_trace(go.Box(
        y=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
        x=x,
        name='rabanete',
        marker_color='#F18436'
    ))
    fig.add_trace(go.Box(
        y=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
        x=x,
        name='cenoura',
        marker_color='#AB851B'
    ))

    fig.update_layout(
        yaxis_title='normalized moisture',
        boxmode='group'  # Agrupe caixas de diferentes traces para cada valor de x
    )
    fig.show()


boxplots()
