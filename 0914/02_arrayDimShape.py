# 배열의 크기(dimension)와 형상(shape)

import numpy as np

data = np.array([[1,2,3],[4,5,6]])
print(data)
# ndarray : n(정수)d(차원)array(배열/행)
print(type(data))

print('rank:', data.ndim) # ndim 속성
print('형상:', data.shape)
print('몇행이니 :', data.shape[0])
print('몇열이니 :', data.shape[1])
print('자료형 :', data.dtype) # int32

print(data[0][0],data[1][1],data[1][2])
print('-'*40)
print(data + data)
print('-'*30)


mylist =[1,2]
print(mylist+mylist)
print('-'*30)

print(data*10)
print('-'*30)

print(data*data)
print('-'*30)

print(1/data)
print('-'*40)

print(data**0.5)
print('-'*30)
print('finished')