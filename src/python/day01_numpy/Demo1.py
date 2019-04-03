
# 1.ndarry

import numpy as np

# vector=np.array(5,10,15,20)

vector=np.array([5,10,15,20])

# array返回的是一个ndarray,numpy特有的数据结构。print后看起来向是一个list的list，就是一个矩阵。
# 看起来是一个list的list，但实际上不是。toStirng是一样的而已
print(vector)

print(type(vector))

# numpy里面提供的函数，可以直接从txt文本里面读取数据，类似于hive里面提供的schema
input= np.genfromtxt("../../resources/day01_numpy/demo.txt", delimiter=",", dtype=str,encoding="utf-8")

print(input)

# shape返回的是形状，结果是一个tuple
print(input.shape)

# 可以直接使用内建函数，help该函数，看函数文档
# print(help(np.array))

array = np.array([[1, 2, 3], [3, 4, 5]])

print(array)

print(type(array))
# 可见，array的作用就是构造矩阵

# 如果只有一行，shape返回的是多少列
n = np.array([1, 3, 4, 5])

print(n.shape)















