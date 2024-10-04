import pandas as pd
from pathlib import Path
import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

def callbacks_graph():
    if not Path.cwd().match('modulo_2_intro'):
        os.chdir(Path.joinpath(Path.cwd(),'modulo_2_intro'))

    csv_file = Path.joinpath(Path.cwd(), 'data','gapminderDataFiveYear.csv')
    df = pd.read_csv(csv_file, sep=',')
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div(
        id="div-1",
        children=[
            dcc.Graph(id="graph-slider-1"),
            dcc.Slider(
                id="year-slider",
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ]
    )

    @app.callback(
        Output('graph-slider-1', component_property="figure"),
        [Input('year-slider', component_property='value')]
    )
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]
        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country",log_x=True, size_max=55)
        fig.update_layout(transition_duration=500)

        return fig

    app.run_server(debug=True, port=8052)

callbacks_graph()