
# single variable distribution analysis

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

x=np.random.normal(size=100000)



print(x)


sns.distplot(x)


plt.show()


iris=sns.load_dataset("iris")

sns.pairplot(data=iris)

plt.show()






