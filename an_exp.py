import pandas as pd # type: ignore
from pathlib import Path
import re
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

def an_exp():
    def format_percent(value):
        return f'{100*value:.2f}%'
    
    def remove_html(html):
        pattern = re.compile('<.*?>')
        cleantext = re.sub(pattern, '', html)
        return cleantext.replace('*', '').strip()

    #Carregamento dos dados e análise prévia
    
    dataset = Path.joinpath(Path.cwd(), 'dataset')
    srp_path = Path.joinpath(dataset, 'survey_results_public.csv')
    srs_path = Path.joinpath(dataset, 'survey_results_schema.csv')
    df = pd.read_csv(srp_path, index_col='ResponseId')
    print(df.head(10))

    print(df.columns)

    df_questions = pd.read_csv(srs_path, index_col='qid')

    print(df_questions.head(10))

    for nome, desc in zip(df_questions['qname'], df_questions['question']):
        print(f'{nome} -> {remove_html(desc)}')
    

    #Tratamento dos dados

    ##Visualização das colunas e dos tipos de dados de cada uma
    ### Object -> podem ser do tipo string
    ### Non-Null Count -> permitem visualizar a quantidade de elementos não-nulos da coluna 

    ### Tipos de dados observados: float64 e object
    print(df.info())

    ##Visualização do total de elementos nulos de cada coluna
    print(df.isna().sum())
    ###Visualização anterior com valores proporcionais, usando função de formatação para porcentagem
    print((df.isna().sum()/len(df)).sort_values(ascending=False).apply(format_percent))
    ###Visualização gráfica dos valores percentuais
    percent_data = (df.isna().sum()/len(df)).sort_values(ascending=False).reset_index()
    print(percent_data.head(5))
    percent_data.columns = ['column_name','percent_na']

    fig,ax = plt.subplots(figsize=(15,5))
    sns.barplot(data=percent_data, x='column_name', y='percent_na')
    fig.suptitle('% de dados faltantes de cada coluna')
    plt.xticks(rotation=80) #roda um pouco os labels de cada coluna
    plt.show()

    # Explorando dados numéricos

    ## Seleção de dados específicos
    print(df.select_dtypes('float')) ##diferencia float de int
    print(df.select_dtypes('number')) ##pega todos os valores numéricos

    ## Métricas dos dados
    print(df.describe()) ##já faz o filtro de números, pois não faz sentido fazer com strings
    print(df.select_dtypes('number').describe().round(2))

    ### Duas colunas estão com valores nulos ou zerados; filtrando colunas úteis
    print(df[['WorkExp','ConvertedCompYearly']].select_dtypes('number').describe().round(2))

    #### NOTA: describe() já desconsidera os valores nulos, entregando uma análise mais correta

    # Explorando dados categóricos
    print(df.select_dtypes('object'))
    ## Conversão de coluna object em string (retorno de nova coluna)
    print(df['RemoteWork'].astype('string'))

    ## Contagem de categorias
    print('')
    print(df['RemoteWork'].value_counts()) #Exclui valores nulos
    print('')
    print(df['RemoteWork'].value_counts(normalize=True, dropna=False)) #entrega resultado como porcentagem de um total; considera valores nulos
    
    ### Contagem cruzada de categorias
    print(df[['Age','RemoteWork']].value_counts().sort_index())

    ### Valores únicos -> para obtenção das categorias existentes
    print(df['RemoteWork'].unique())

   

    

an_exp()
