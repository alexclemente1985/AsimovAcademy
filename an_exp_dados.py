import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder


# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

def an_exp_dados():
    mapbox_token = Path.joinpath(Path.cwd(), "mapbox", "mapbox_default_public_token.txt")
    dataset = Path.joinpath(Path.cwd(), "datasets", "sao-paulo-properties-april-2019.csv")
    print(mapbox_token)
    px.set_mapbox_access_token(open(mapbox_token).read())

    df_data = pd.read_csv(dataset)

    print(df_data.head())

    df_rent = df_data[df_data["Negotiation Type"] == "rent"]
    print(df_rent.head())
    # se aparecer coluna object onde deveria ser numérica, existe algum erro a ser tratado
    print(df_rent.info())

    print(df_rent.describe())

    fig = px.scatter_mapbox(df_rent, lat="Latitude", lon="Longitude", color="Price", size="Size",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, opacity=0.4)

    fig.update_coloraxes(colorscale=[[0, 'rgb(166,206,227, 0.5)'],
                                     [0.02, 'rgb(31,120,180,0.5)'],
                                     [0.05, 'rgb(178,223,138,0.5)'],
                                     [0.10, 'rgb(51,160,44,0.5)'],
                                     [0.15, 'rgb(251,154,153,0.5)'],
                                     [1, 'rgb(227,26,28,0.5)']
                                     ],
                         )

    fig.update_layout(height=800, mapbox=dict(center=go.layout.mapbox.Center(lat=-23.543138, lon=-46.69486)))

    fig.show()

    df_rent.hist(bins=30, figsize=(30, 15))
    plt.show()

    print(df_rent["Property Type"].value_counts())
    print(df_rent["District"].value_counts())
    print(df_rent.corr(numeric_only=True)["Price"].sort_values(ascending=False))

    # Preparando dados para machine learn
    ## Dados abaixo não agregam ao aumento da inteligência
    df_cleaned = df_rent.drop(["New", "Property Type", "Negotiation Type"], axis=1)

    ## Tratamento de variáveis categóricas de texto

    ### Ordinal Encoder
    ####Pode não ser a melhor escolha devido à enorme quantidade de classes na coluna, podendo confundir o modelo
    ordinal_encoder = OrdinalEncoder()
    district_encoded = ordinal_encoder.fit_transform(df_rent[["District"]])
    print(district_encoded)

    ### One hot encoded
    ####Criação de uma coluna para cada bairro, e colocar 0 ou 1 para dizer se registro é ou não do bairro
    cat_encoder = OneHotEncoder()
    housing_cat_1hot = cat_encoder.fit_transform(df_rent[["District"]])
    #####Cada linha vai corresponder a um apartamento, e cada coluna um bairro; se o apto pertencer ao bairro o valor será 1
    print(housing_cat_1hot.toarray())

    ### Pandas get_dummies
    #### Faz algo parecido com o One Hot Encoded, porém já criando um dataframe com as novas colunas que representam os bairros
    one_hot = pd.get_dummies(df_cleaned["District"])

    df = df_cleaned.drop("District", axis=1)
    df = df.join(one_hot)

    print(df.head())


an_exp_dados()
