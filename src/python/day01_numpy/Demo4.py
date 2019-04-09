 # numpy常用函数

import numpy as np

array=np.arange(15)

print(array)
print(array.ndim)


print(array.shape)

array=array.reshape([3,5])

print(array)
print(array.shape)
print(array.ndim)


# 初始化空矩阵,传的是tuple
zeros = np.zeros((3, 5))

print(zeros.shape)

print(zeros)

# 初始化单位矩阵
ones=np.ones((3,5),int)
print(ones.shape)
print(ones)


ones=np.arange(1,30,10)

print(ones)


# 随机数或者是随机矩阵
random = np.random.random((2, 3))

print(random.shape)
print(random)

# 区间个数
arange=np.linspace(0,10,100,dtype=str)

print(arange.shape)
print(arange)



# 矩阵之间的加减法

a=np.array([10,20,30,40])

b=np.arange(4)

print(a)
print(b)

print(a-b)


# 平方
print(a**2)

print(np.random.random((2,3))*20>10)

a=np.array([[1,2,3],[2,3,4]])
b=np.ones((3,2))

# *是对应位置的乘法
# print(a*b)

print(a.shape)
print(b.shape)

# 矩阵乘法
print(a.dot(b))





