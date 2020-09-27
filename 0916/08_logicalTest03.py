# 훈련데이터와 테스트 데이터를 7:3으로 분리
# 최종 결과에 대하여 정확도를 구함
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = '../logisticexample/logicalTest03.csv'

data=np.loadtxt(filename, delimiter=',', dtype=np.int32)

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

#seed =1
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)# ,random_state=seed)

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column,activation='sigmoid'))

learning_rate=0.01
sgd = tf.keras.optimizers.SGD(lr=learning_rate)
model.compile(loss='binary_crossentropy', optimizer=sgd)

model.fit(x=x_train,y=y_train, epochs=200,batch_size=10,verbose=1)

total, hit = 0,0 # 총 갯수, 맞춘 갯수

for idx in range(len(x_test)):
    result = model.predict_classes(np.array([x_test[idx]]))
    print('테스트용 데이터 : %s' % (x_test[idx]))
    print('정답 : %s ' % y_test[idx], end=' ')
    print('예측값 : %s ' % str(result.flatten()))

    total +=1
    # 예측값과 정답이 같은경우 1추가
    hit += int(y_test[idx] == result.flatten())
    print('-'*30)

print('총 갯수: {}, 맞춘 갯수: {}'.format(total,hit))
accuracy = hit/total
print('정확도 = %.4f' % (accuracy))

print('finished')
