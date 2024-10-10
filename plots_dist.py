import seaborn as sns
from matplotlib import pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#%matplotlib inline

def plots_dist():
    tips = sns.load_dataset('tips')

    print(tips)

    sns.distplot(tips['total_bill'])
    plt.show()

    sns.distplot(tips['total_bill'], kde=False, bins=300)
    plt.show()

    #cria gráfico com dois outros, mostrando uma relação entre ambos
    sns.jointplot(x="total_bill", y="tip", data=tips)
    plt.show()

    #análise com regressão linear
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    plt.show()

    #análise com hexadecimal (tipo um mapa)
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
    plt.show()

    #Criação de matriz de correlação com todas as variáveis numéricas
    sns.pairplot(tips)
    plt.show()

    #Criação de matriz de correlação com todas as variáveis numéricas, com segregação por categorias
    sns.pairplot(tips, hue="sex")
    plt.show()

    #Criação de matriz de correlação com todas as variáveis numéricas, com segregação por categorias (customização cor)
    sns.pairplot(tips, hue="sex", palette="coolwarm")
    plt.show()

     #Marca a aparição dos pontos no gráfico (observação da concentração dos pontos)... usado em conjunto com outros gráficos
    #sns.regplot(tips["total_bill"])
    #plt.show()

     #Cria uma estimativa a partir das aparições do regplot, gerando um gráfico de distribuição normal
    sns.kdeplot(tips["total_bill"])
    #sns.regplot(tips["total_bill"])
    plt.show()

plots_dist()