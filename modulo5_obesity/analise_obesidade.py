from pathlib import Path

import pandas as pd
import numpy as np


def analise_obesidade():
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    data_obesity = pd.read_csv(Path.joinpath(datasets, 'obesity_cleaned.csv'))

    print(data_obesity.info())
    print(data_obesity.head())

    # data_obesity["Obesity"] = data_obesity[]


analise_obesidade()
