# 텍스트 파일을 읽어서 sqlite DB에 추가하기

filename='../attach/mem.txt'

myfile = open(file=filename,mode='r',encoding='utf-8')
mylist = [item.strip() for item in myfile.readlines()]
print(mylist)
myfile.close()

import sqlite3

conn = sqlite3.connect('../0908/sqlitedb.db')
mycursor = conn.cursor()

sql = """insert into members(id,name) values(?,?)"""
for item in mylist:
    columnlist = item.split(',')
    mycursor.execute(sql, columnlist)


conn.commit()



mycursor.close()
conn.close()

print('finished')