# https://cafe.naver.com/ugcadman/1113 아이리스데이터
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt



filename='../logisticexample/iris.csv'

data = pd.read_csv(filename)#, header=None)
print(data.shape)
print('-'*30)

print(data.columns)
print('-'*40)

x_data = data[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
y_data = data[['Name']]

# 총 150행 중에서 훈련 105행, 테스트 45

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data, test_size=0.3)

# 데이터 속성들의 값의 차이가 너무 크면 학습이 잘 안됨
# StandardScaler 클래스를 사용하여 평균 0, 표준편차 1인 표준정규 분포로 표준화를 수행


scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)


model = LogisticRegression()
model.fit(x_train,y_train)

train_score = model.score(x_train,y_train)
print('train 정확도 : %.3f' %(train_score))

test_score = model.score(x_test,y_test)
print('test 정확도 : %.3f' %(test_score))

print('회귀 계수')
print(model.coef_)
print(model.intercept_)



print('test result')
prediction = model.predict(x_test)

# confusion_matrix(정답데이터, 예측값)
cf_matrix = confusion_matrix(y_test, prediction)
print('confusion_matrix :')
print(cf_matrix)
print('='*30)


# accuracy :  정확도를 구해주는 함수
accuracy = accuracy_score(y_test, prediction)
print('accuracy(정확도): %.3f' %(100*accuracy))
print('@'*30)

# 주요 분류와 관련된 metrics(지표)에 대한 보고서
cl_report = classification_report(y_test,prediction)
print(cl_report)



plt.rc('font',family='applegothic')


sns.heatmap(pd.DataFrame(cf_matrix), annot=True, cmap='YlGnBu',fmt='g')

plt.title('counfusion matrix')
plt.ylabel('actual label')
plt.xlabel('predicition label')

filename='03_logisticRegression01_01.png'
plt.savefig(filename)
print(filename +' 파일이 저장되었습니다.')

'''
csv 파일을 이용하여 데이터를 읽음
학습용 데이터와 훈련용 데이터를 7:3으로 나눔
데이터를 정규화 함 (StandardScaler)
StandardScaler 클래스를 사용하여 평균 0, 표준편차 1인 표준정규 분포로 표준화를 수행
정확도를 구해보자
cunfusion matrix 및 각 지표에 대하여 확인
HeatMap 을 그려보자
'''