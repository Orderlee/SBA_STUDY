import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
filename ='../logisticexample/surgeryTest.csv'
data = np.loadtxt(filename, delimiter=',')

print(data.shape)
table_col = data.shape[1]
y_column = 1
x_column = table_col - 1

x = data[:, 0:x_column]
y = data[:, x_column:]

#seed = 0
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2)#,random_state=seed)

model = Sequential()

model.add(Dense(units=30, input_dim=x_column, activation='relu'))
model.add(Dense(units=y_column,activation='sigmoid'))

# 정확도('accuracy')를 보여줌
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])

model.fit(x_train,y_train, epochs=400, batch_size=10, verbose=1) # epochs 횟수를 바꾸면 real,prediction 값이 달라

# 모델 관련 속성
# input 텐서의 정보
print(model.inputs)
print('-'*30)

# output 텐서의 정보
print(model.outputs)
print('-'*30)

# model.add() 함수를 사용한 레이어드의 주소 정
print(model.layers)
print('-'*30)

# metrics : 성능에 대한 지표
# 기본값으로 비용함수됨('loss')는 무조건 보여줌
# 더 추가하려면 compile 함수의 매개변수 metrics에 리스트 형식으로 넣어주면 됨
print(model.metrics_names)
print('-'*30)

pred = model.predict_classes(x_test)
for idx in range(len(pred)):
    label = y_test[idx]
    print('real : %f, prediction : %f' % (label,pred[idx]))

print('완료하였습니다.')
