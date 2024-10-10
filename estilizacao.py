import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def estilizacao():
    tips = sns.load_dataset('tips')

    print(tips)

    sns.set_style("white")
    sns.countplot(x='sex', data=tips)
    plt.show()

    sns.set_style("ticks")
    sns.countplot(x='sex', data=tips, palette='deep')
    plt.show()

    sns.set_style("darkgrid")
    sns.countplot(x='sex', data=tips, palette='deep')
    plt.show()

    sns.set_style("dark")
    sns.countplot(x='sex', data=tips, palette='deep')
    plt.show()

    sns.set_style("whitegrid")
    sns.countplot(x='sex', data=tips, palette='deep')
    plt.show()

    fig,ax = plt.subplots(figsize=(20,8))
    sns.countplot(x='sex', data=tips, palette='deep', ax=ax)
    ax.set_xlabel('Eixo x')
    plt.show()

    sns.set_context('poster', font_scale=4)
    sns.countplot(x='sex', data=tips, palette='coolwarm')
    plt.show()



estilizacao()