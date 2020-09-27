# 사이킷런을 이용한 회귀분석
# 결정계수 : 실제값이 예측값과 어느정도의 일치성을 보이는지 나타내는 척도
#           값은 0부터 1사이의 값으로, 1에 가까우면 설명력이 좋다.
# R-squared = 1-Σ(y-H)**2/Σ(y-bary)**2
# y는 실제정답
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

plt.rc('font',family='applegothic')
# 학습용 데이터셋
filename='../regress_example/linearTest01.csv'
# skiprows : 머리글 1행은 제외
training = np.loadtxt(filename, delimiter=',',skiprows=1)
print(training)

x_column = training.shape[1] - 1

x_train = training[:, 0:x_column]
y_train = training[:,x_column:]

# 모델 객체 생성()
model = LinearRegression()

model.fit(x_train,y_train)

print('기울기(w) : ', model.coef_) # w 값
print('절편(b) : ', model.intercept_) #b값

# residual(잔차)
print('차의 제곱 합 (cost) : ', model._residues)

# 시각화
plt.title('그래프')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_train,y_train,'bo') # 'k.':검정색 점

train_pred = model.predict(x_train)
plt.plot(x_train,train_pred, 'r') #회귀선

filename= 'linearRegression01.png'
plt.savefig(filename)
print(filename + ' 파일을 저장하였습니다.')

# 테스트용 데이터셋
filename='../regress_example/linearTest02.csv'
# skiprows : 머리글 1행은 제외
testing = np.loadtxt(filename, delimiter=',',skiprows=1)
#print(testing)

x_column = testing.shape[1] - 1

x_test = testing[:, 0:x_column]
y_test = testing[:,x_column:]

#print(y_test)
# 산술 연산에 의한 결정계수 구하기
y_test_mean = np.mean(np.ravel(y_test))

# TSS) 편차의 제곱의 총합 (TSS(total sum of square))
TSS = np.sum((np.ravel(y_test)-y_test_mean)**2)

# RSS) 회귀식과 평균값의 차이의 총합 (RSS(residual sum of squares))
RSS = np.sum((np.ravel(y_test)-np.ravel(model.predict(x_test)))**2)

# 결정계수 = 1- RSS/TSS
R_squared = 1-(RSS/TSS)

print('R_squared 01:', R_squared)
print('R_squared 02:', model.score(x_test,y_test))


print('finished')