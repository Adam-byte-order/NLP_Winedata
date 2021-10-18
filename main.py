from sklearn.datasets import make_regression
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats
import time
import datetime

# Funcio per a llegir dades en format csv
def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset


if __name__ == '__main__':
    # Visualitzarem només 3 decimals per mostra
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    # Carreguem dataset
    dataset = load_dataset('Winery.csv')
    data = dataset.values