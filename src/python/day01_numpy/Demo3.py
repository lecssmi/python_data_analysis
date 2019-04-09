# numpy矩阵基础


import numpy as np


vector=np.array(['1','2','3'])

print(vector.dtype)

print(vector)

vector=vector.astype(float)

print(vector)
print(vector.dtype)

print(vector)

print(vector.min())


matrix=np.array([[1,2,3],[2,3,4],[3,4,5]])

# 对行求和

print(matrix)
print(matrix.sum(axis=1))

print(matrix.sum(axis=0))

print(help(matrix.sum))