"""
출력결과
이름: 김철수
주민 번호: 121225-3456789
성별: 남자
나이: 8세
체크: 미성년자(19세이상이면 성년)
 슬라이싱과 if 구문 등을 이용하여 다음과 같이 출력해보세요.
"""
#내가 짠 코드
name='김철수'
ssn='121225-3456789'

print('이름:',name,sep='')
print('주민번호:',ssn,sep='')

gen=ssn[7]
#print(gen)

if gen =='1' or gen =='3':
    print('성별:'+'남성')
else:
    print('성별:'+'여성')

age=20-int(ssn[:2])
print('나이:', '%d세' % age,sep='')

if age > 19:
    print('체크:'+'성')
else:
    print('체크:'+'미성년자')


#선생님이 짠 코드
print('-'*30)
dpos1= ssn[7]

# if dpos1 =='1' or dpos1 =='3' :
#     gender ='남자'
# else:
#     gender ='여자'

if dpos1 in ['1','3']:
    gender ='남자'
else:
    gender ='여자'

apos2 =int(ssn[0:2]) #출생연도 2자리 수
# birth_year : 출생연
if dpos1 in ['1','2']:
    birth_year= 1900+apos2
else:
    birth_year=2000+apos2

now=2020

age= now - birth_year

if age >= 19:
    remark = '성인'
else:
    remark = '미성년자'

print('이름: %s' % name)
print('주민번호: %s' % ssn)
print('성별: %s' % gender)
print('나이: %d세' % age)
print('체크: %s' % remark)