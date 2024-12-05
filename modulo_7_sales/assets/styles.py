import dash_bootstrap_components as dbc

tab_card = {'height': '100%'}

main_config = {
    'hovermode':'x unified',
    'legend': {'yanchor':'top',
               'y':0.9,
               'xanchor':'left',
               'x':0.1,
               'title':{'text': None},
               'font':{'color': 'white'},
               'bgcolor':'rgba(0,0,0,0.5)'},
    'margin': {'l':10,'r': 10, 't':10,'b':10}
}

config_graph = {"displayModeBar": False, 'showTips': False}

template_theme1 = 'flatly'
template_theme2 = 'darkly'
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY