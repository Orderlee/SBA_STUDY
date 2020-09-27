test_acc = [0.9245,0.9215,0.9785,0.9685,0.9739]
test_loss = [0.2782,0.2818,0.0764,0.1113,0.0931]
comments = ['테스트01','테스트02','테스트03','테스트04','테스트05']

mycolor = ['b','g','r','c','b']

import matplotlib.pyplot as plt

plt.rc('font',family='applegothic')

plt.figure()
plt.title('테스트 케이스별 정확도')
plt.xlabel('테스트 케이스')
plt.ylabel('정확도')
plt.bar(comments, test_acc, color=mycolor)

filename='mnist accuracy graph.png'
plt.savefig(filename)
print(filename + ' 저장 되었습니다..')

plt.figure()
plt.title('테스트 케이스별 손실 함수')
plt.xlabel('테스트 케이스')
plt.ylabel('손실함수')
plt.bar(comments, test_loss, color=mycolor)

filename='mnist loss graph.png'
plt.savefig(filename)
print(filename + ' 저장 되었습니다..')
print('끝')