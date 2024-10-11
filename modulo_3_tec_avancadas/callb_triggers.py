import dash
from dash import html, dcc, Input, Output, ctx, callback_context
import pdb

def callb_triggers():
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.Button('Button 1', id='btn-1-ctx-example'),
        html.Button('Button 2', id='btn-2-ctx-example'),
        html.Button('Button 3', id='btn-3-ctx-example'),
        html.Div(id='container-ctx-example')
    ])


    @app.callback(Output('container-ctx-example','children'),
                  Input('btn-1-ctx-example', 'n_clicks'),
                  Input('btn-2-ctx-example', 'n_clicks'),
                  Input('btn-3-ctx-example', 'n_clicks'))
    def display(btn1, btn2, btn3):
        #Usar o pdb.set_trace() para poder debugar e entender como funciona o callback_context e o motivo da igualdade abaixo
        #pdb.set_trace()
        ## triggered[0] permite pegar o último elemento acionado na tela, e da forma abaixo consegue-se obter o id do mesmo
        button_clicked = callback_context.triggered[0]['prop_id'].split('.')[0]

        return html.Div([
            dcc.Markdown(
                f'''You last clicked button with ID {button_clicked}
                ''' if button_clicked else '''You haven't clicked any button yet''')
        ])

    app.run_server(debug=True)

callb_triggers()