
# 基础操作

import seaborn as sns

import numpy as np

import  matplotlib.pyplot as plt

import matplotlib as mpt


fig=plt.figure()

x=np.linspace(-np.pi,np.pi,100)

for i in range(100):
    plt.plot(x,np.sin(x)*(i*0.1),c="black")

sns.despine()
plt.show()






