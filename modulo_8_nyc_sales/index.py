from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from app import app

from dataset import dataset

from components._map import map_comp
from components._histogram import histogram
from components._controllers import controller

from pathlib import Path

def index():

    #Data ingestion
    df_data, mean_lat, mean_long = dataset()

    #Layout
    map = map_comp()
    hist = histogram()
    controllers = controller()[0]
    slider_size = controller()[1]

    app.layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([controllers], md=3),
                dbc.Col([map, hist], md=9)
            ])
        ], fluid = True
    )

    #Callbacks
    @app.callback(
            [
                Output('hist-graph', 'figure'),
                Output('map-graph', 'figure')
            ],
            [
                Input('location-dropdown', 'value'),
                Input('slider-square-size', 'value'),
                Input('dropdown-color', 'value')
            ]
        )
    def update_histogram(location, square_size, color_map):
        if location is None:
            df_intermediate = df_data.copy()
        else:
            df_intermediate = df_data[df_data['BOROUGH'] == location] if location != 0 else df_data.copy()
            size_limit = round(slider_size[square_size], 1) if square_size is not None else round(df_data['GROSS SQUARE FEET'].max(),1)
            df_intermediate = df_intermediate[df_intermediate["GROSS SQUARE FEET"] <= size_limit]
        
        hist_fig = px.histogram(df_intermediate, x=color_map, opacity=0.75)
        hist_layout = go.Layout(
            margin=go.layout.Margin(l=10, r=0, t=0, b=5),
            showlegend=False,
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        hist_fig.layout = hist_layout

        #homogeneizando a distribuição de cores com numpy
        color_map = "SALE PRICE"
        colors_rgb = px.colors.sequential.GnBu

        df_quantiles = df_data[color_map].quantile(np.linspace(0,1, len(colors_rgb))).to_frame()
        df_quantiles = (df_quantiles - df_quantiles.min())/(df_quantiles.max() - df_quantiles.min())
        df_quantiles['colors'] = colors_rgb

        color_scale = [[i,j] for i, j in df_quantiles['colors'].items()]

        px.set_mapbox_access_token(open(Path.joinpath(Path.cwd(), 'keys', 'mapbox_key')).read())

        map_fig = px.scatter_mapbox(
                df_intermediate, 
                lat= "LATITUDE", 
                lon="LONGITUDE", 
                color=color_map, 
                size="size_m2", 
                size_max=20, 
                zoom=10, 
                opacity=0.4
            )
        
        map_fig.update_layout(mapbox=dict(center=go.layout.mapbox.Center(lat=mean_lat, lon=mean_long)),
                              template="plotly_dark", paper_bgcolor="rgb(0,0,0,0)",
                              margin=go.layout.Margin(l=10, r=10, t=10, b=10))
        
        map_fig.update_coloraxes(colorscale = color_scale)
        
        return hist_fig, map_fig



    app.run_server(debug=True, port=8051)

index()

