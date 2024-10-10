import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def plots_reg():
    tips = sns.load_dataset('tips')

    print(tips)

    #Regressão linear
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex")
    plt.show()

    ## Diferenciando cada categoria com marcadores
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", markers=['o','v'])
    plt.show()

    ## Diferenciando cada categoria com marcadores, alterando o tamanho deles
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", markers=['o','v'], scatter_kws={'s': 100})
    plt.show()

    ## Criando gráficos em relação a uma outra propriedade (no caso "time" e "day")
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", col="time")
    plt.show()
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", col="time", row="day")
    plt.show()

    ## Ajustando à tela de visualização
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", markers=['o','v'], scatter_kws={'s': 100}, aspect=1.6, height=8)
    plt.show()

plots_reg()