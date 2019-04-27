
# color

import numpy as np

import  matplotlib.pyplot as plt

import  matplotlib as mpl

import seaborn as sns


import pandas as pd


# when we use seaborn, it is necessary to call pyplot.show() method

sns.set_style("whitegrid")

data=np.random.normal(size=(20,6))+np.arange(6)/2

print(data)

sns.boxplot(data=data)

plt.show()


