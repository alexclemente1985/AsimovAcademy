import plotly.express as px

def polar_bar_charts():
    df = px.data.wind()
    fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.show()

polar_bar_charts()