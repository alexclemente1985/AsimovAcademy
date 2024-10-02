import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def intro_dash():
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    df = pd.DataFrame({
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })

    fig = px.bar(df, x="Fruit", y="Amount",color="City")

    app.layout = html.Div(id="div1",
                          children=[
                              html.H1("Hello Dash", id="h1", style={"color":"#FF00FF"}),
                              html.Div("Dash: Um framework web para Python"),
                              dcc.Graph(figure=fig, id="Graph1")
                          ])

    app.run_server(debug=True, port=8052)


if __name__ =="__main__":
    intro_dash()
