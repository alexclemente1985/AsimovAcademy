import plotly.express as px

def graficos_alternativos():
    df = px.data.gapminder().query("year == 2007")
    fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                      color='lifeExp', hover_data=['iso_alpha'])
    fig.show()

graficos_alternativos()