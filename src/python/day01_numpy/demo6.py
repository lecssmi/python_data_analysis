# 不同复制操作对比
import numpy as np

a=np.arange(10)
b=a
print(b==a)

# 一个对象
print(b is a)

print(id(a))

print(id(b))


# view,类似于sql中的视图

c=a.view()

print(c is a)

print(a.shape)
print(c.shape)

a=a.reshape((2,-1))

print(a.shape)
print(c.shape)


# 深度复制
d=a.copy()

print(a is d)

print(a)


# 最大值所在的索引值
print(a.argmax(axis=0))

print(a.argmax(axis=1))


#
a=np.arange(0,40,10)

# 扩充
b=np.tile(a,(2,3))

print(b)


