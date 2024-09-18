import plotly.graph_objects as go

import numpy as np


def histogramas():
    np.random.seed(1)

    x = np.random.randn(500)

    fig = go.Figure(data=[go.Histogram(x=x)])
    fig.update_layout(height=500)
    fig.show()

    # Sobreposição de histogramas
    x0 = np.random.randn(500)
    # Adicione 1 para deslocar a média da distribuição x0
    x1 = np.random.randn(500) + 1

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=x0))
    fig.add_trace(go.Histogram(x=x1))

    # Sobreposição
    fig.update_layout(barmode='overlay')

    # Reduz a opacidade para que possamos ver ambos histogramas
    fig.update_traces(opacity=0.75)
    fig.show()


histogramas()
