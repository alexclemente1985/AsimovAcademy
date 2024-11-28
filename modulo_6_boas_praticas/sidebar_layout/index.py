from app import *
from pages import page1, page2
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
import sidebar

app.layout = html.Div(children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Location(id="url"),
                        sidebar.layout
                    ], md=2, xs=2, sm=2, lg=2, xl=2, style={"width": "20vw"}),
                    dbc.Col([
                        html.Div(id="page-content")
                    ], style={"width":"80vw"})
                ],style={"display":"flex", "flex-direction":"row"})
            ], style={"padding": "0px"})



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    print(pathname)
    if pathname == "/":
        return page1.layout
    else:
        return page2.layout


if __name__ =="__main__":
    app.run_server(port=8050, debug=True)


