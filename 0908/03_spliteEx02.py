import sqlite3


conn = sqlite3.connect(database='sqlitedb.db')

mycursor=conn.cursor()
try:
    # execute : sql 구문을 실행하는 함수
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError as err:
    print("테이블이 존재하지 않습니다.")

mycursor.execute('''create table sungjuk
(id text, subject text , jumsu integer, unique(id,subject))
''')

datamylist=[('lee','java',10),('lee','html',20),('lee','python',30),('jo','java',40),
            ('jo','html',50),('jo','pytho ',60),('ko','java',70),('ko','html',80),
            ('ko','python',90)]

sql = "insert into sungjuk(id, subject, jumsu) values(?,?,?)"

mycursor.executemany(sql, datamylist)
conn.commit()