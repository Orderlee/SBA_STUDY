import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename ='../regress_example/multiLinear01.csv'
data= np.loadtxt(filename, delimiter=',')

print(data.shape)

table_col=data.shape[1]
y_column =1
x_column =table_col -y_column # 3-1 = 2

x = data[:,0:x_column]
y = data[:,x_column:]

seed = 0
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=seed)

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column,activation='linear'))
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(x_train,y_train,epochs=5000,batch_size=10,verbose=1)

# 가중치 정보를 출력해줌
print(model.get_weights())

prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]
    pred = prediction[idx]

    print('real : %f, prediction: %f' % (label,pred))

print('finished')



