# 손글씨 데이터셋을 다운로드하고, 데이터의 구조를 살펴보자
# 임의의 하나의 데이터를 이용하여 시각화

from tensorflow.python.keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

print('x_train.shape:', x_train.shape)
print('@'*30)

print('x_train.dtype:', x_train.dtype)
print('@'*30)

print('x_train.ndim:', x_train.ndim)
print('@'*30)

print('y_train:', y_train)
print('@'*30)

print('x_test.shape:', x_test.shape)
print('@'*30)

print('len(y_test):', len(y_test))
print('@'*30)

print('y_test:', y_test)
print('@'*30)

import matplotlib.pyplot as plt

digit = x_train[4]
plt.imshow(digit)
filename='mnist_image.png'
plt.savefig(filename)
print(filename +' 저장하였습니다.')


print('끝')