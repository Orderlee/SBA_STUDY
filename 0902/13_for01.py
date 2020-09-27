# range() 함수 : 반복문에서 특성 횟수만큼 요소들을 반복 시키고자 할 때 사용
# range([start,],end,[,step])

for idx in range(1,11):
    print(idx)
print('-'*30)

for idx in range(11):
    print(idx)
print('-' * 30)

for idx in range(1,10,2):
    print(idx)
print('-'*30)

for idx in range(10,1,-1):
    print(idx)
print('-'*30)

# 1부터 10까지의 총합 구하기
total= 0

for idx in range(1,11):
    total += idx

print('총합:%d' % total)

print('-'*30)

#1 + 4+ 7 + 10+...+100 =1717
total = 0
for idx in range(1,101,3):
    total +=idx
print('총합01:%d' % total)

print('-'*30)

#97+92_87+...+7+2=990
total=0
for idx in range(97,1,-5):
    total += idx

print('총합02:%d' % total)
print('-'*30)

#1*1+6*6+11*11+..._96*96=63670
total =0
for idx in range(1,97,5):
    total += pow(idx,2)
    #total += idx **2
    #total +=idx*idx
print('총합03:%d' % total)

# 사용자가 숫자를 하나 입력 받고, 1부터 해당 수까지의 총합 구하기
# 숫자 입력 :5
# 출력 결과 : 1부터 5까지의 합은 55 입니다.
print('-'*30)

# abs(): 절대값으로 변경해주는 함수
print(abs(-15))

#만약 음수 값을 입력하면 절대값으로 변경 하도록 합니다.
#숫자입력 :-10

num=abs(int((input('숫자를 넣으세요.:'))))
total=0
for idx in range(1,num+1):
    #print(idx)
    total += idx

print('출력결과:'+'1부터 %d까지의 합은 %d입니다.' % (num,total))

print('-'*30)

num=int(input('숫자를 넣으세요.:'))
total=0
for idx in range(1,num+1):
    #print(idx)
    total += idx

print('출력결과:'+'1부터 %d까지의 합은 %d입니다.' % (num,total))
print('-'*30)

num=int(input('숫자를 넣으세요.:'))
if num <0:
    num = abs(num)

total=0

for idx in range(1,num+1):
    #print(idx)
    total += idx

print('출력결과:'+'1부터 %d까지의 합은 %d입니다.' % (num,total))
