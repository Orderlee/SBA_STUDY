# 모듈을 사용하고자 할때 import 키워드 사용
import random # random 모듈 :  랜덤한 데이터를 추출하고자 할 때 사용하는 모듈
# for idx in range(1,11):
#     answer = random.randint(1,100);
#     print(answer)

# answer = 컴퓨터가 기억한 값
answer = random.randint(1,100)
print('정답: %d' % answer)

cnt=0 #시도 횟수
while True:
    # su 우리가: 입력한 숫
    su = int(input('1부터 100사이의 정수 1개 입력:'))
    cnt += 1 #시도 횟수를 1증가
    if answer > su:
        print('%d보다 큰 수를 입력하세요.' % su)
    elif answer < su:
        print('%d보다 작은 수를 입력하세요.' % su)
    else:
        print('정답입니다.')
        print('%d번만에 맞췄습니다.' % cnt)
        break
print('finished')

