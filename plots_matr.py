import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#HEATMAPS - Mapas de calor

def plots_matr():
    flights = sns.load_dataset('flights')

    print(flights)

    # Reorganiza tabela definindo colunas índice, para preparar para plot matricial
    df_flights_matrix = flights.pivot_table(index="year", columns="month", values="passengers")

    # Mapa de calor: duas variáveis categóricas e uma variável contínua representada pelo eixo z
    fig, ax = plt.subplots(figure=(20,8))
    sns.heatmap(df_flights_matrix, ax=ax)
    plt.show()

    ## Colocando os valores do eixo z em cada um dos blocos do mapa
    fig, ax = plt.subplots(figure=(20,8))
    sns.heatmap(df_flights_matrix, ax=ax, annot=True, fmt=".0f", linewidths=1, cmap="magma")
    plt.show()

    # Cluster map - reorganiza índices e colunas para encontrar correlações entre os dados

    sns.clustermap(df_flights_matrix)
    plt.show()





plots_matr()