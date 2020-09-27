# 함수의 마지막에는 return 구문이 들어감
# 만약 명시되지 않으면 return None라는 구문이 숨어있음

# None 리턴하지 않는 , 의미가 없는
# void, vacant,empty, no response

def namePrint(name,age):
    print('{}님의 나이는 {}살입니다.'.format(name,age))
    return None

name='제시카'
age=20
result =namePrint(name,age)
print(result)

if result ==None:
    print('데이터를 구하지 못했습니다.')
else:
    print('참~~잘 했어요.')

print('-'*30)

def gugudan(su):
    rng = range(1,10) #1부터 9까지
    for i in rng:
        print('{}x{}={}'.format(su,i,(su*i)))

dan=3
gugudan(dan)
print('-'*30)

# 2,4,7 출력해 보세요.

mylist=[2,4,7]

for i in range(0,len(mylist)):
    gugudan(mylist[i])
    print('-'*30)

# 2단이면[2,4,6,...,10] 출력되는 함수를 만들어 보세요.

def Gugu(n):
    result=[ n*idx for idx in range(1,10)]
    print(result)

su=2
print(Gugu(su))
print('-'*30)

# 2단부터 4단까지 각 단의 결과를 list 형식으로 출력해 보시오.

def gugu2(n,m):
    for x in range(n,m+1):
        result=[x*idx for idx in range(1,10)]
        print(result)
        print('*'*40)

n,m=2,4
print(gugu2(2,4))

print('finished')