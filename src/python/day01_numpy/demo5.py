 # 矩阵常用操作

import numpy as np

b=np.arange(10)

print(b)

print(np.exp(b))

print(np.square(b))

random=np.random.random((3,4))*10
print(random)

# 将矩阵flatmap成一个向量
print(random.ravel())

print(random.ravel().reshape((3,4)))

# 转置

print(random.T)


# reshape中猜测,-1就是占位符
print(random.reshape((4,-1)))


a=np.floor(np.random.random((3,4))*10)
b=np.ceil(np.random.random((3,4))*10)


# 横着 拼接
print(np.hstack((a,b)))
# 竖着拼接
print(np.vstack((a,b)))

# 拆分

print("!!!")
print(np.hsplit(a,2))







