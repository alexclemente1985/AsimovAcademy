import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import modal_novo_processo, modal_novo_advogado, modal_advogados


### Layout

layout = dbc.Container([])

### Callbacks

#### Atualização dropdown advogados

#### Atualização dropdown clientes

#### Atualização dropdown processos

#### Geração de conteúdo dos cards