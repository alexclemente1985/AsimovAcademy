# This is a sample Python script.
from pathlib import Path
from random import sample

import numpy as np
import matplotlib.pyplot as plt


def matplotlib():
    if not Path.joinpath(Path.cwd(), "graficos").exists():
        Path.mkdir(Path.joinpath(Path.cwd(), "graficos"))

    # Criação de 11 valores distribuídos entre os números 0 e 5
    x = np.linspace(0, 5, 11)
    y = x ** 2

    print(f"x: {x} | y: {y}")

    plt.plot(x, y, 'green')
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.title("Teste de plot")
    plt.show()

    # subplot: permite a criação de mais de um gráfico em um mesmo plot
    # Parâmetros: Quantidade de linhas, colunas e index do eixo a ser editado no momento
    plt.subplot(1, 2, 1)
    # r---: vermelho tracejado
    plt.plot(x, y, 'r--')
    plt.subplot(1, 2, 2)
    # b*--: azul com asterisco e tracejado
    plt.plot(y, x, 'b*--')
    plt.show()

    fig = plt.figure()

    # Adição de eixo na figure
    # Parâmetros
    ## primeiro: percentual da parte da esquerda aonde gráfico irá se posicionar
    ## segundo: percentual da parte inferior aonde o gráfico irá se posicionar
    ## terceiro: largura
    ## quarto: altura
    ### Abaixo: 10% à esquerda, 10% do fundo, 80% do valor da figure como largura e altura
    axes = fig.add_axes((0.1, 0.1, 0.8, 0.8))
    axes.plot(x, y, 'orange')
    axes.set_xlabel("Label x")
    axes.set_ylabel("Label y")
    axes.set_title("Teste figures")
    plt.show()

    fig2 = plt.figure()

    axes2 = fig2.add_axes((0.1, 0.1, 0.8, 0.8))
    axes2.plot(x, y, 'orange')
    axes2.set_xlabel("Label x")
    axes2.set_ylabel("Label y")
    axes2.set_title("Teste Figures Primeiro Eixo")

    axes3 = fig2.add_axes((0.2, 0.5, 0.4, 0.3))
    axes3.plot(y, x, 'purple')
    axes3.set_xlabel("Label x")
    axes3.set_ylabel("Label y")
    axes3.set_title("Teste Figures Segundo Eixo")
    plt.show()

    # Subplots -> permite desacoplamento de tupla gerando figure e eixo

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r--')
    ax.set_title("Teste de subplots")
    plt.show()

    fig2, ax2 = plt.subplots(nrows=1, ncols=2)
    for axis in ax2:
        axis.plot(x, y, 'g--')
    # Ajusta o gráfico na tela
    plt.tight_layout()
    plt.show()

    fig3, ax3 = plt.subplots(nrows=1, ncols=2, figsize=(30, 8))
    ax3[0].plot(x, y, 'yellow')
    ax3[1].plot(y, x, 'b*--')

    plt.show()

    fig4, ax4 = plt.subplots(nrows=2, ncols=2)
    ax4[0][0].plot(x, y, 'yellow')
    ax4[0][1].plot(x, y, 'g*--')
    ax4[1][0].plot(x, y, 'red')
    ax4[1][1].plot(y, x, 'b*--')

    plt.show()

    # Customização

    fig5 = plt.figure()
    ax5 = fig5.add_axes((0, 0, 1, 1))
    ax5.plot(x, x ** 2, 'b--', label='x**2', alpha=0.5)
    ax5.plot(x, x, 'b--', label='x', alpha=1)

    ax5.plot(x, x ** 3, color="#FF50AB", label='x**3')
    ax5.set_title("Título Gráfico Customizado")
    ax5.set_xlabel("Eixo X")
    ax5.set_ylabel("Eixo Y")

    ax5.legend(loc='center left')


    # Salvando a figura
    fig5.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_customizado.png"), dpi=200)

    # Linhas e estilos de marcador
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(x, x + 1, color="red", linewidth=0.25)
    ax.plot(x, x + 2, color="red", linewidth=0.50)
    ax.plot(x, x + 3, color="red", linewidth=1.00)
    ax.plot(x, x + 4, color="red", linewidth=2.00)

    # Possiveis estilos de linha: ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
    ax.plot(x, x + 5, color="green", lw=3, linestyle='-')
    ax.plot(x, x + 6, color="green", lw=3, ls='-.')
    ax.plot(x, x + 7, color="green", lw=3, ls=':')

    # Traços estilizados
    line, = ax.plot(x, x + 8, color="black", lw=1.50)
    line.set_dashes([5, 10, 15, 10])  # Formato: comprimento da linha, comprimento do espaço, ...

    # possíveis símbolos de marcador: marcador = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
    ax.plot(x, x + 9, color="blue", lw=3, ls='-', marker='+')
    ax.plot(x, x + 10, color="blue", lw=3, ls='--', marker='o')
    ax.plot(x, x + 11, color="blue", lw=3, ls='-', marker='s')
    ax.plot(x, x + 12, color="blue", lw=3, ls='--', marker='1')

    # tamanho e cor do marcador
    ax.plot(x, x + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
    ax.plot(x, x + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)
    ax.plot(x, x + 15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
    ax.plot(x, x + 16, color="purple", lw=1, ls='-', marker='s', markersize=8,
            markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")

    fig.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_Linhas.png"), dpi=200)

    # Intervalos de distância
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    axes[0].plot(x, x ** 2, x, x ** 3)
    axes[0].set_title("intervalos de eixos padrão")

    axes[1].plot(x, x ** 2, x, x ** 3)
    axes[1].axis('tight')
    axes[1].set_title("eixos apertados")

    axes[2].plot(x, x ** 2, x, x ** 3)
    axes[2].set_ylim([0, 60])
    axes[2].set_xlim([2, 5])
    axes[2].set_title("distância personalizada dos eixos")

    fig.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_Distancias.png"), dpi=200)
    plt.close(fig)
    # Gráficos especiais
    # Scatter
    fig_sc = plt.figure()
    axes_sc = fig_sc.add_axes((0,0,1,1))
    axes_sc.scatter(x, y, marker="+")
    fig_sc.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_Scatter.png"), dpi=200)
    plt.close(fig_sc)


    # Histograma
    data = sample(range(1,1000), 100)
    fig_hist = plt.figure()
    axes_hist = fig_hist.add_axes((0,0,1,1))
    axes_hist.hist(data)
    fig_hist.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_Histograma.png"), dpi=200)
    plt.close(fig_hist)

    #Boxplot
    fig_box = plt.figure()
    axes_box = fig_box.add_axes((0,0,1,1))
    data = [np.random.normal(0, std, 100) for std in range(1,4)]
    axes_box.boxplot(data)
    fig_box.savefig(Path.joinpath(Path.cwd(), "graficos", "Grafico_Boxplot.png"), dpi=200)
    plt.close(fig_box)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matplotlib()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
