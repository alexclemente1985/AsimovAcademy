import plotly.express as px

def graficos_estatisticos():
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)
    fig.show()

    df = px.data.tips()
    fig = px.box(df, x="day", y="total_bill", color="smoker", notched=True)
    fig.show()

    df = px.data.iris()
    fig = px.density_heatmap(df, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")
    fig.show()

graficos_estatisticos()