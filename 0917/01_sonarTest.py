# 돌과 광물 정보를 저장한 CSV 파일
# 7:3 분리 작업 후 학습 결과를 파일 형식으로 저장
# 정답(label) 컬럼이 문자열 ('R','M')로 구성이 되어 있으므로, 학습시키면
# 숫자 형식으로 변경
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# data = ['갑','을','병','정','을','갑']
#
# le = LabelEncoder() # 객체 생성
# le.fit(data) # 피팅
#
# result = le.transform(data)
#
# print(result)
filename= '../logisticexample/sonarTest.csv'

df = pd.read_csv(filename,header=None)
# print(df.head())
# print('-'*30)
#
# print(df.info())
# print('-'*30)

data = df.values # 데이터 프레임 ndarray로 변경

table_col = data.shape[1]
y_column = 1
x_column = table_col -1

x = data[:,0:x_column]
y_imsi = data[:,x_column]

# print(y_imsi)
# print('-'*30)

le = LabelEncoder()
le.fit(y_imsi)
y = le.transform(y_imsi) # .ravel()

# print(y)
# print('-'*30)

x = x.astype(np.float)
y = y.astype(np.float)


seed = 0
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=seed)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()

model.add(Dense(units=24, input_dim=x_column, activation='relu'))
model.add(Dense(units=10,activation='relu'))
model.add(Dense(units=y_column,activation='sigmoid'))

# metrics :성능지표
# metrics=['accuracy'] : 정확도도 출력해줌

# 손실함수: [평균 제곱 오차], [크로스(교차) 엔트로피]
# 교차 엔트로피 방식은 출력 값에 로그를 취하여, 오차가 매우 큰 경우에는 빨리 수령
# 오차가 적어지면 속도를 감속하도록 만들어진 알고리
# MSE:'mean_squared_error'
# MAE:'mean_absolute_error'
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=200,batch_size=5,verbose=1)

print('모델을 파일 형식으로 저장합니다.')
model.save('my_model.h5')

# 저장해둔 모델은 load_model() 을 사용하여 읽어 들일 수 있음
print(model.metrics_names)

# evaluate : 테스트 모드에서 수행된 loss value, metrics value를 반환해 줌
score = model.evaluate(x_test,y_test)
print('train loss : %.4f' % (score[0]))
print('train accuracy : %.4f' % (score[1]))

print('완료하였습니다.')

