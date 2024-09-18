import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plotly_intro():
    #Figure: caixa onde todos os gráficos vão ficar inseridos
    ## Contém Data, Layout e Frames
    ### Data: Dados necessários para criação dos gráficos (podem ser dicionários ou objetos)
    ### Layout: permite ajustes de dimensões
    ### Frames: raro, usado em casos específicos como animação

    fig = go.Figure(
        data=[go.Bar(x=[1,2,3], y=[1,2,3])],
        layout=go.Layout(
            title=go.layout.Title(text="Uma Figure Especificada como um Objeto Gráfico")
        )
    )
    fig.show()

    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(go.Bar(y=[1,2,3], x=[6,5,2], marker_color="green"), row=1, col=1)
    fig.add_trace(go.Scatter(y=[8, 2, 4,5], x=[6, 5, 2, 7], marker_color="red", mode="lines"), row=1, col=2)

    fig.update_layout(title_text="Usando update_layout()", title_font_size=20)
    fig.show()

    fig.show()

    #Gráficos em um mesmo box
    fig = go.Figure(
        data=[
            go.Bar(x=[1, 2, 3], y=[1, 2, 3]),
            go.Scatter(y=[0,3,2], mode="lines")
        ]
    )
    fig.update_layout(height=700)
    fig.show()

    fig = go.Figure(
        data=[
            go.Bar(x=[1, 2, 3], y=[1, 3, 2]),
        ]
    )

    #Alteração das bordar do gráfico
    fig.data[0].marker.line.width = 4
    fig.data[0].marker.line.color = "black"
    fig.show()


if __name__ == '__main__':
    plotly_intro()
