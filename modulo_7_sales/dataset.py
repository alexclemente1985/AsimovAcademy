from pathlib import Path
import pandas as pd


df = pd.read_csv(Path.joinpath(Path.cwd(),'data', 'dataset_asimov.csv'))
df_crude = df.copy()

# ==== Conversão de meses em números para economia de memória ==== #

df.loc[ df['Mês'] == 'Jan', 'Mês'] = 1
df.loc[ df['Mês'] == 'Fev', 'Mês'] = 2
df.loc[ df['Mês'] == 'Mar', 'Mês'] = 3
df.loc[ df['Mês'] == 'Abr', 'Mês'] = 4
df.loc[ df['Mês'] == 'Mai', 'Mês'] = 5
df.loc[ df['Mês'] == 'Jun', 'Mês'] = 6
df.loc[ df['Mês'] == 'Jul', 'Mês'] = 7
df.loc[ df['Mês'] == 'Ago', 'Mês'] = 8
df.loc[ df['Mês'] == 'Set', 'Mês'] = 9
df.loc[ df['Mês'] == 'Out', 'Mês'] = 10
df.loc[ df['Mês'] == 'Nov', 'Mês'] = 11
df.loc[ df['Mês'] == 'Dez', 'Mês'] = 12

# ==== Limpezas e conversões para inteiro (redução de consumo de memória) ==== #

df['Chamadas Realizadas'] = df['Chamadas Realizadas'].astype(int)
df['Dia'] = df['Dia'].astype(int)
df['Mês'] = df['Mês'].astype(int)
df['Valor Pago'] = df['Valor Pago'].str.lstrip('R$ ')
df['Valor Pago'] = df['Valor Pago'].astype(int)
df.loc[df['Status de Pagamento'] == 'Pago', 'Status de Pagamento'] = 1
df.loc[df['Status de Pagamento'] == 'Não pago', 'Status de Pagamento'] = 0
df['Status de Pagamento'] = df['Status de Pagamento'].astype(int)

# ==== Opções de filtros ==== #

options_month = [{'label': 'Ano todo', 'value': 0}]

for i, j in zip(df_crude['Mês'].unique(), df['Mês'].unique()):
    options_month.append({'label': i, 'value': j})

options_month = sorted(options_month, key=lambda x: x['value']) 
options_team = [{'label': 'Todas Equipes', 'value': 0}]

for i in df['Equipe'].unique():
    options_team.append({'label': i, 'value': i})

# ========= Função dos Filtros ========= #
    
def month_filter(month):
    if month == 0:
        mask = df['Mês'].isin(df['Mês'].unique())
    else:
        mask = df['Mês'].isin([month])
    return mask

def team_filter(team):
    if team == 0:
        mask = df['Equipe'].isin(df['Equipe'].unique())
    else:
        mask = df['Equipe'].isin([team])
    return mask

def convert_to_text(month):
    match month:
        case 0:
            x = 'Ano Todo'
        case 1:
            x = 'Janeiro'
        case 2:
            x = 'Fevereiro'
        case 3:
            x = 'Março'
        case 4:
            x = 'Abril'
        case 5:
            x = 'Maio'
        case 6:
            x = 'Junho'
        case 7:
            x = 'Julho'
        case 8:
            x = 'Agosto'
        case 9:
            x = 'Setembro'
        case 10:
            x = 'Outubro'
        case 11:
            x = 'Novembro'
        case 12:
            x = 'Dezembro'
    return x

