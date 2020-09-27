#함 무한 whileloop : 반복횟수가 몇번인지 모른 경우
# 어느조건을 충족하면 break 구문을 사용하여 반드시 종료해야
# cnt=0
# while True:
#     print('a'+str(cnt))
#     cnt+=1
#     if cnt ==5:
#         break
#
# print('finished')

# 사용자가 입력한 시험점수에 대한 평균과 개수를 구해봅시다.
# 음수 값이 입력되면 프로그램을 종료하도록 합니다.

total =0 #총점
count =0 #시험 본 횟수
average =0.0 #평균점수


while True:
    score = int(input('점수를 입력하세요.'))
    if score <=0:
        break
    total += score
    count += 1

average = total/count

print('총 시험 횟수: {}'.format(count))
print('총점: {}'.format(total))
print('평균: %.3f'% average)

print('finished')