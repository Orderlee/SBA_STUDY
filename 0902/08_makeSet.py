mylist=[1,1,1,2,2,3,3,3,4,4,5]
print(len(mylist))

# 집합: 중복을 허락하지 않는 자료 구조
# 관련함수: set()
# 특징: 합집합, 교집합, 차집합등의 함수 제공
# 집합도 결과물에 중괄호를 사용
# 함수 : add(), update(), remover(),
myset = set(mylist)
print(myset)

newlist= list(myset)
print(newlist)

print('-'*30)

set1 = set([1,2,3])
print(set1)

print('-'*30)

set1.add(4)
print(set1)

print('-'*30)

set1.update([5,6,7])
print(set1)

print('-'*30)

set1.remove(4)
print(set1)

print('-'*30)

set3 = set([1,2,3,4])
set4 = set([3,4,5,6])

set5 = set3.intersection(set4)
print(set5)

print('-'*30)

set6 = set3.union(set4)
print(set6)

print('-'*30)

set7 = set3.difference(set4)
print(set7)

print('-'*30)

# 차집합은 교환 볍칙이 성립하지 않는다.
# set3 - set4 와 set4-set3은 다르다

set8 = set4.difference(set3)
print(set8)

print('-'*30)

# 다음은 어떤 자료 구조로 표현하면 좋을까?
# 1) 회원가입 정보(아이디는'hong'이고,이름은'홍길동',주소는'마포 공덕'입니다.) :dict
# 2) 로또 번호 생성기 : set
# 3) 게시물의 제목 정보 : list



