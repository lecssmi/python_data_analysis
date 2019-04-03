# numpy基础结构


import numpy as np


array=np.array([1,2,3,4])

print(type(array))

# numpy.array()里面的参数类型都应该是一样的,能够尽量向上造型，转换成一个更加通用的格式

print(array.dtype)


array=np.genfromtxt("../../resources/day01_numpy/demo.txt",delimiter=",",encoding="utf-8",dtype=str)

print(array.dtype)

print(array)

print("~~~~~")
print(array[0,1:])

print(array[:,1:3])

print(array[:,2:])
# 也就是说，ndarray也是支持切片操作的。


vector=np.array([1,2,3,4])

# 如果对ndarray进行判断操作，就是对每个元素进行操作，相当于是for循环。
print(vector==3)

result=vector>1

print(result[2:4])

# ndarray的索引也可以是一个数组
print(vector[result])

print(vector[[1,2,3]])










