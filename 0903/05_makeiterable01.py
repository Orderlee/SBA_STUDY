#iterable : 반복할 수 있는, 반복가능한
# list, tuple, dict 문자열

# list comprehension, set comprehension, dict comprehension
mylist01=[idx for idx in range(1,5)]
print(mylist01)

print('-'*25)

mylist02=[2 * idx for idx in range(1,5)]
print(mylist02)

print('-'*25)

#1,4,7...100
mylist03=[idx for idx in range(1,101,3)]
print(mylist03)
print(sum(mylist03)) #min, max
print(min(mylist03))
print(max(mylist03))

print('-'*25)

mylist04=[idx for idx in range(1,101,3) if idx % 10 ==0]
print(mylist04)

print('-'*25)

# 1 부터 10까지의 정수중에서 3의 배수가 아닌 수들의 총합 37
mylist05=[idx for idx in range(1,11) if idx % 3!=0]
print(mylist05)
print(sum(mylist05))

print('-'*25)

#중첩 for
mylist06=[x*y for x in range(2,10) for y in range(1,10)]
print(mylist06)

print('-'*25)

mylist=[('김',10),('이',20),('최',30)]
mydict={ data[0]:data[1] for data in mylist}
print(mydict)

print('-'* 25)

students=[('이순신',90,80),('김유신',70,40)]
# students를 사용하여 다음과 같
# 은 사전을 만드시오
# '이순신':(80,90),'김유신':(70,40)

mydict={data[0]:data[1:] for data in students}
print(mydict)