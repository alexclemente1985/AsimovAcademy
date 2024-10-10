import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def plots_categ():
    tips = sns.load_dataset('tips')

    print(tips)

    #Gráfico em barras
    sns.barplot(x="sex",y="total_bill", data=tips)
    plt.show()

    ## Uso do desvio padrão no lugar da média, do caso anterior
    sns.barplot(x="sex",y="total_bill", data=tips, estimator=np.std)
    plt.show()

    #Gráfico de barras baseado na contagem
    sns.countplot(x="sex", data=tips)
    plt.show()

    #Gráfico de caixas (box) usando percentis de dados
    ## Linha central: mediana dos dados
    ## Pontinhos acima do gráfico: outliers (pontos "fora da curva", que podem ser descartados)
    sns.boxplot(x="day", y="total_bill", data=tips, palette='rainbow')
    plt.show()

    ## Orientação na horizontal
    sns.boxplot(x="total_bill", y="day", data=tips, palette='rainbow', orient="h")
    plt.show()

    ## Com categorização por sexo
    sns.boxplot(x="sex",y="total_bill", data=tips, palette='rainbow', hue="sex", orient="v")
    plt.show()

    # Semelhante ao boxplot, porém vendo kde
    sns.violinplot(x="sex",y="total_bill", data=tips, palette='rainbow')
    plt.show()

    ## Violinplot com categorização
    sns.violinplot(x="sex",y="total_bill", data=tips, palette='rainbow', hue="sex")
    plt.show()

    ## Com espelhamento para economia de espaço
    sns.violinplot(x="sex",y="total_bill", data=tips, palette='rainbow', hue="sex", split=True)
    plt.show()

    ## Permite uma comparação de concentrações dos valores
    sns.swarmplot(x="day",y="total_bill", data=tips)
    plt.show()

plots_categ()