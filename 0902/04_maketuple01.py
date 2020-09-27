# 튜플(tuple): 목록이라는 측면에서 리스트와 유사
# 단, 값에 대하여 읽기 전용, 리스트보다 빠름
# 관련함수: tuple()
# 인덱싱,슬라이싱 가능
# 소괄호를 사용
# + 연산자 : 튜플을 합쳐 주는 기낭
# * 연산자 : 해당 튜플의 요소들 반

tuple1 = (1,2,3)

tuple1=tuple1+(4, ) # 튜플 합치기
print(tuple1)

print('-'*30)

tuple2=1,2,3,4
mylist=[1,2,3,4]
tuple3= tuple(mylist)

if tuple2 == tuple3:
    print('yes')
else:
    print('no')

print('-'*30)

tuple4=(1,2,3)
tuple5=(4,5,6)

tuple6=tuple4+tuple5
print(tuple6)

tuple7=tuple4*3
print(tuple7)

print('-'*30)

# swap : 두 변수간의 값을 상호 맞바꿈하는 것
a,b = 10, 20
a,b = b,a
print(a)
print(b)

print('-'*30)

# 슬라이싱
tuple8=(1,2,3,4,5,6)
print(tuple8[1:3])
print(tuple8[3:])

# tuple8[0]=100 --> 읽기전용이라 쓰기는 안됨

