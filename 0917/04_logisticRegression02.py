import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

filename='../logisticexample/titanic.csv'

data = pd.read_csv(filename)
print(data.columns)
print(data.shape)
print('-'*30)

# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

# 코딩 변경 ) 데이터분서겡 맞도록 사용자가 값을 변경하는 작
print(data['Sex'].unique()) # 중복된 데이터는 배제하고 1개만 표
data['Sex'] =data['Sex'].map({'female':1, 'male':0})
print(data['Sex'].unique())

# 결측치(missing value) : 누락된 데이터
# 출력결과에 nan 이라고 표현되는 부분
print(data['Age'].unique())

# 결측치에 대하여 나머지 항목들의 평균값으로 치환
# fillna : 결측치(na)를 채워 넣기(fill)
data['Age'].fillna(value=data['Age'].mean(), inplace=True)
print(data['Age'].unique())

print(data['Pclass'].unique()) # 좌석등급

result = data.groupby('Pclass')['Pclass'].count()
print('좌석 등급별 인원수')
print(result)

# dummy 컬럼 만들기
# 파생 컬럼 생성: FirstClass(1등석일때만 값 1), SecondClass(2등석일때만 값 2)

# FirstClass 컬럼에는 Pclass의 값이 1일때만 1을 , 나머지는 0으로 채움
data['FirstClass'] = data['Pclass'].apply(lambda x:1 if x ==1 else 0)

# SecondClass 컬럼에는 Pclass의 값이 2일때만 2를 , 나머지는 0으로 채움
data['SecondClass'] = data['Pclass'].apply(lambda x:1 if x ==2 else 0)

# 성별과 나이와 일등석|이등석 정보를 이용하여 생존 여부 판단하기
x_data =data[['Sex','Age','FirstClass','SecondClass']]
y_data = data['Survived']

# 데이터 셋 분리 작업

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data)


# 정규화


scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

# fit_transform 함수를 사용하여 이미 한번 fit 했으므로 두번째 문장에서는
# transform 함수만 호출하면 됨
x_test = scaler.transform(x_test)

# 모델 생성하기


model = LogisticRegression()
model.fit(x_train, y_train)

# 주의 : 상관분석은 인과 관계가 아니라 연관성과 관련 있음

# coef_는 w값을 의미
# 회귀분석에서 w의 의미는 y에 데이터 대한 인과 관계의 정도를 의미
# 성별과 일등석 탑승 여부가 생사를 판단하는데 가장 영향력을 많이 준다고 볼 수 있
print(model.coef_)
print('-'*30)

print(model.intercept_)
print('-'*30)

# 샘플데이터로 예측하기
# ['Sex','Age','FirstClass','SecondClass']
soo = np.array([0.0,20.0,0.0,0.0])
hee = np.array([1.0,17.0,1.0,0.0])
minho = np.array([0.0,32.0,1.0,0.0])
sample = np.array([soo,hee,minho])

print(sample)

sample = scaler.transform(sample)

print(sample)

print(model.predict(sample))

# probability : 확률(P)
proba = model.predict_proba(sample)
print(proba)
print(type(proba))



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

filename='04_logisticRegression02_01.png'
plt.savefig(filename)
print(filename +' 파일이 저장되었습니다.')