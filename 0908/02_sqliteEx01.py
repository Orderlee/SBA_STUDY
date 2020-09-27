# sqlite : 소형 개인용 데이터 저장을 위한 데이터베이

import sqlite3

# conn : 데이터베이스에 접근하기 위한 객체
# database: 데이터베이스 파일 이름
conn = sqlite3.connect(database='sqlitedb.db')

print(type(conn))

# cursor(커서): 데이터 베이스 작업을 수행하고 있는 메모리 공간
mycursor = conn.cursor()

try:
    # execute : sql 구문을 실행하는 함수
    mycursor.execute("drop table students")
except sqlite3.OperationalError as err:
    print("테이블이 존재하지 않습니다.")

# primary key: 필수이면서 동시에 같은 값을 가질 수 없는 컬럼
mycursor.execute('''
create table students
(id text primary key, name text, birth text)
''')
sql ="insert into students(id, name, birth) values('lee','이승기','1989/11/11')"
mycursor.execute(sql)

sql ="insert into students(id, name, birth) values('kang','강감찬','1111/11/11')"
mycursor.execute(sql)

datamylist=[('jo','조용필','1985/12/31'),('ko','고아라','1969/06/09'),('sim','심형래','1969/07/04')]

# ?를 place holder 라고 함, 치환되어야 할 어떠한 대상
# 데이터 유형에 상관 없이 외따옴표 적지 마라
sql="insert into students(id, name, birth) values(?,?,?)"
#mycursor.executemany(sql=sql,seq_of_parameters=datamylist)
mycursor.executemany(sql,datamylist)
conn.commit()

findID='ko'
sql="select * from students where id='%s'" % (findID)

mycursor.execute(sql)

result =mycursor.fetchone()
print(result)

if result != None :
    print('아이디 :' +result[0], end='')
    print(',이름 :' +result[1],end='')
    print(',생일 :' +result[2],end='')
else:
    print('문제가 있습니다.')
print('-'*30)

sql='select * from students order by name desc' # asc<->desc

for id,name,birth in mycursor.execute(sql):
    print(id+'$' + name + '$'+birth)
print('-'*30)

sql ="select * from students where name like '%이%'"
mycursor.execute(sql)
print(mycursor.fetchall())

# 'id'가 lee인 친구의 이름을 '이문세로 바꾸세요.
pid='lee'
newname='이문세'
sql="update students set name='%s' where id='%s'"
mycursor.execute(sql %(newname,pid))

conn.commit()

#'id'가 sim인 친구의 데이터를 삭제

pid='sim'
sql = "delete from students where id='%s'"
mycursor.execute(sql %(pid))
conn.commit()

# asc는 명시하지 않아도 됨
sql='select * from students order by name asc'

for id,name,birth in mycursor.execute(sql):
    print(id+'$' + name + '$'+birth)
print('-'*30)



mycursor.close()
conn.close()
print('finished')

# like 연산자: whidcard를 사용한 조회
# whidcard 문자
# _(언더바)는 1글자를 의미
# %는 0개 이상 무한개 이하를 의미
# 이%: 성씨가 이씨인 사람
# %이: 이름의 끝이 '이'로 끝나는 사람
# %이%: 이름에 '이'가 들어있는 사람
# fetch(패치): 내용물의 요소를 바깥으로 꺼내는 동작
    # fetchone(), fetchall()


