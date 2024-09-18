import plotly.graph_objects as go
import numpy as np

def pie():
    labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()

    #Estilizando gráficos de pizza
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig = go.Figure(data=[go.Pie(labels=['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio'],
                                 values=[4500, 2500, 1053, 500])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.show()

    #Destacando elementos individuais do gráfico
    labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
    values = [4500, 2500, 1053, 500]

    # pull is given as a fraction of the pie radius
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
    fig.show()

pie()