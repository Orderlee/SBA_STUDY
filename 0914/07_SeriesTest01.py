# Series : 1차원적인 동일한 타입의 데이터 묶음
# 엑셀 파일의 특정한 1개의 컬럼 정보
from pandas import Series

mylist = [10,40,30,20]

# 색인을 지정하지 않으면 0부터 순차적으로 숫자로 지정
myseries = Series(mylist)
print(myseries)
print('-'*15)

# 색인을 지정하려면, index 매개 변수를 사용
myseries = Series(mylist, index=['강감찬','이순신','김유신','광해군'])
#기 색인에 이름 지정하기
myseries.index.name = '이름 점수'

# 시리즈 자체에 이름 지정하기
myseries.name = '학생들 시험'
print(myseries)
print('-'*16)


print(type(myseries))
print('-'*17)

# 문자열의 dtype은 'object'입니다.
print(myseries.index)
print('-'*18)

# 색인의 값을 출력
print(myseries.values)
print('-'*19)

for idx in myseries.index:
    print('색인:' + idx +', 값 : ' + str(myseries[idx]))

print('-'*20)