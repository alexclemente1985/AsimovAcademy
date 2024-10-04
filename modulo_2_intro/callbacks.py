import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

def callbacks():
    app = dash.Dash(__name__)

    app.layout = html.Div(
        id="div-1",
        children=[
            html.H6("Altere o valor abaixo para ver o callback em ação!" ,style={"font-size":"20px", "color":"green"}),
            html.Div(
                id="input-div-1",
                children=[
                    html.Label("Entrada: "),
                    dcc.Input(id="input-1", type="text", value="Valor inicial")
                ]
            ),
            html.Br(),
            html.Div(
                id="output-1"
            )
        ]
    )

    #Permite acionar a função abaixo dentro da propriedade do componente com o id alvo, linkando valores entre componentes do mesmo
    @app.callback(
            Output(component_id="output-1", component_property="children"),
            [Input(component_id="input-1", component_property="value")]
    )
    def update_output_div(value):
        return f"Saída: {value}"


    app.run_server(debug=True, port=8052)


callbacks()