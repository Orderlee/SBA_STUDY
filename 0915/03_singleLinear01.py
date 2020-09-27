'''
첨부한 csv파일을 읽어온다.
훈련/학습 데이터와 테스트 데이터의 비율을 75:25로 분리
훈랸/학습 데이터를 이용하여 선형회귀 분석을 한 다음,
테스트 데이터를 이용하여 결과를 예측해봄
'''
import numpy as np
# sklearn : science kit (머신러닝을 하기 위한 패키지)
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename='../regress_example/singleLinear01.csv'
data = np.loadtxt(filename, delimiter=',')
print(type(data))

table_col = data.shape[1] #컬럼수
y_column = 1 # 출력(정답) 데이터 컬럼수
x_column = table_col - y_column # 입력 데이터 컬럼

x = data[:,0:x_column]
y = data[:,x_column:]
print(x)
print('-'*30)

print(y)
print('-'*30)

# 입력용학습, 입력용테스트, 출력용학습, 출력용테스트 = train_test_split(입력원본,출력원본,test_size=테스트데이터의 비율)
# 일반적으로 7:3

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
print(x_train)
print('-'*30)

print(y_train)
print('-'*30)

# 모델을 생성하고, 학습을 수행
# 단계 01 : 모델(작업공간) 생성
model = Sequential()

# 단계 02: 레이어를 추가
# 총 레이어 갯수 : add() 함수 개수 + 1
# Dense : 레이어를 추가할때 사용하는 클래스
# units = 출력값의 크기, input_dim = 입력데이터의 크기 , activation ='활성화 함수'
# 'linear' : 선형회귀분분석
model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))

# 단계 03: 컴파일 수행
# loss : 비용(손실) 함수를 지정
# optimizer : 옵티마이저로서, 경사 하강법을 잘 수행하기 위한 가이드
model.compile(loss='mean_squared_error',optimizer='adam')

# 단계 04: 훈련/학습 진행 (기출 문제 풀기)
# epochs: 반복횟수
# batch_size : 1번에 수행할 데이터의 양
# verbose: 0(진행 결과를 출력하지 않음),1(기본값), 2(epoch 당 1번만)
# 교사 학습법 : 입력 데이터와 출력(정답) 데이터를 같이 넣어주는 학습법
model.fit(x_train,y_train, epochs=5000, batch_size=10, verbose=1)

# 단계 05: 예측 진행 (새로운 문제 풀기)
prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx] #정답 데이터
    pred = prediction[idx] #예측치

    print('real : %f, prediction : %f' % (label, pred))


print('finished')