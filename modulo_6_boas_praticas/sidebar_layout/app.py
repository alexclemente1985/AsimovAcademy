import dash
import dash_bootstrap_components as dbc

#dbc_css = ("https://cdn.jsdelivr.net/ht/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")

app = dash.Dash(__name__, external_scripts=[dbc.themes.MINTY])

app.scripts.config.serve_locally = True
server = app.server