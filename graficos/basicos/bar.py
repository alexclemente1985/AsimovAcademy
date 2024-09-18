import plotly.graph_objects as go
import numpy as np


def bar():
    animais = ['Girafas', 'Macacos', 'Tigres']

    fig = go.Figure(data=[
        go.Bar(name='Zoo SP', x=animais, y=[20, 14, 23]),
        go.Bar(name='Zoo RS', x=animais, y=[12, 18, 29])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    # Change the bar mode
    #Empilhando barras
    fig.update_layout(barmode='stack', height=600)
    fig.show()

    #Estilizando barras individualmente
    colors = ['lightslategray', ] * 5
    colors[1] = 'crimson'

    fig = go.Figure(data=[go.Bar(
        x=['Item A', 'Item B', 'Item C',
           'Item D', 'Item E'],
        y=[20, 14, 23, 25, 22],
        marker_color=colors
    )])

    fig.update_layout(title_text='Item menos usado')
    fig.show()


bar()
