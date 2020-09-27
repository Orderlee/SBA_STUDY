from pandas import Series

myindex =['서울','부산','광주','대구','울산','목포','여수']
mylist =[50,60,40,80,70,30,20,]
myseries = Series(data = mylist, index= myindex)
print(myseries)
print('-'*15)

print(myseries['대구'])
print(type(myseries['대구']))
print('-'*20)

print(myseries[['대구']])
print(type(myseries[['대구']]))
print('-'*21)

# 문자열 색인으로 슬라이싱 하는 경우 양쪽 모두 포함 됨
print(myseries['대구':'목포'])
print('-'*22)

print(myseries[[2]])
print('-'*23)

# 콜론으로 슬라이싱하는 경우에는 대괄호 1개
print(myseries[0:5:2])
print('-'*24)

# 콤마를 사용하는 경우 대괄호 2개
print(myseries[[1,3,5]])
print('-'*25)

myseries[2]=22 # 쓰기
print(myseries)
print('%'*26)

myseries[2:5] = 33
print(myseries)
print('%'*27)

# 서울과 대구만 55로 변경
myseries[['서울','대구']] = 55
print(myseries)
print('%'*28)

myseries[0::2] = 77
print(myseries)
print('%'*30)

#그래프 그려보기