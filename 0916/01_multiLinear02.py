import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

# 출력 1개이고, 입력은 n (n>=1)

# csv 데이터 불러오기
filename = '../regress_example/multiLinear02.csv'

data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1] #4
y_column = 1
x_column = table_col - y_column # 4-1 = 3

# 입력과 출력 데이터 분리
x = data[:, 0:x_column]
y = data[:, x_column:]

# 훈련용 데이터셋과 테스트용 데이터 셋 분리
seed=1
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.3,random_state=seed)

# 모델생성
model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column,activation='linear'))
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(x_train,y_train, epochs=5000, batch_size=10, verbose=1)

print(model.get_weights())

prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]
    pred = prediction[idx]

    print('real :%f, prediction: %f' % (label,pred))

print('finished')
