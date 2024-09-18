import plotly.express as px
def scatter_area_line_bar():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig.show()


    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
                     marginal_x="box", trendline="ols", template="simple_white")
    fig.show()


    df = px.data.tips()
    fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", facet_row="time", facet_col="day",
                 category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
    fig.show()


    df = px.data.iris()
    fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
                            color="species")
    fig.show()


    df = px.data.gapminder()
    fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     hover_name="country", log_x=True, size_max=60)
    fig.show()


    df = px.data.gapminder()
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                     size="pop", color="continent", hover_name="country", facet_col="continent",
                     log_x=True, size_max=45, range_x=[100, 100000], range_y=[25, 90])
    fig.show()

scatter_area_line_bar()