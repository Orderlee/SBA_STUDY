import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = '../logisticexample/logicalTest02.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x_train = data[:,0:x_column]
y_train = data[:,x_column:]

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column,activation='sigmoid'))

learning_rate =0.1
sgd = tf.optimizers.SGD(lr=learning_rate)

model.compile(loss='binary_crossentropy',optimizer=sgd)

model.fit(x=x_train,y=y_train, epochs=2000,batch_size=10,verbose=0)

H = model.predict(x_train)
print(H)
print('-'*30)
# 0 : 강아지, 1: 고양이
x_test = [[2,1],[6,7],[11,6]]

def getCategory(mydata):
    mylist =['강아지','고양이']
    print('예측 : %s ,%s' % (mydata,mylist[mydata[0]]))





# flatten() : 차원을1 차원으로 만들어주는 함
for item in x_test:
    H2 = model.predict(np.array([item]))
    print(H2.flatten())
    print('-'*30)

    pred = model.predict_classes(np.array([item]))
    # pred = np.argmax(model.predict(np.array([item])),axis=1)
    print('테스트 데이터:', np.array([item]))
    getCategory(pred.flatten())
    print('*'*30)

print(pred)

print('finished')