import plotly.graph_objects as go
import numpy as np

def mesh3d():
    np.random.seed(1)

    N = 70

    fig = go.Figure(data=[go.Mesh3d(x=(70 * np.random.randn(N)),
                                    y=(55 * np.random.randn(N)),
                                    z=(40 * np.random.randn(N)),
                                    opacity=0.5,
                                    color='rgba(244,22,100,0.6)'
                                    )])

    fig.update_layout(
        width=700)

    fig.show()

mesh3d()