# 중첩 리스트
# 중첩된 갯수만큼 대괄호를 사용하면 됨
saram01=['hong','홍길동',20,'용산']
saram02=['kim','김철수',30,'마포']
saram03=['kang','강남',40,'구로']

mylist=[]
mylist.append(saram01)
mylist.append(saram02)
mylist.append(saram03)
print(mylist)

print('-'*30)

print(mylist[1][2])
mylist[2][1]='강호동'
print(mylist)

mylen=len(mylist)
# 세사람의 평균 나이 구하기

sum=mylist[0][2]+mylist[1][2]+mylist[2][2]
avg=sum/mylen
print('합계:',sum)
print('평균:%.2f' % avg)

# '홍길동$김철수$강호동' 출력해보기(join함수)
name=[]
mylen=len(name)
name.append(mylist[0][1])
name.append(mylist[1][1])
name.append(mylist[2][1])
print('$'.join(name))

