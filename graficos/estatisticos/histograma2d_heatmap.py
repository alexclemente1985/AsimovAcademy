import plotly.graph_objects as go

import numpy as np


def histograma2d_heatmap():
    np.random.seed(1)

    x = np.random.randn(500)
    y = np.random.randn(500) + 1

    fig = go.Figure(go.Histogram2d(
        x=x,
        y=y
    ))
    fig.show()

    # Heatmap
    fig = go.Figure(data=go.Heatmap(
        z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
        x=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
        y=['Manhã', 'Tarde', 'Noite'],
        hoverongaps=False))
    fig.show()


histograma2d_heatmap()
