# mystudent.xml 파일을 읽어서 students.csv 파일을 만들기
# students.db 파일에 students 테이블을 생성하고,
# 데이터를 추가
# pandas.DataFrame,sqlite3,xml 패키지 사
# 추가사항 : 총점과 평균도 같이 csv파일과 테이블에 저장

from pandas import DataFrame
import sqlite3
from xml.etree.ElementTree import parse

tree= parse('../attach2/mystudent.xml')
myroot=tree.getroot()
#print(myroot)

allstudents = myroot.findall('student')

totallist=[]
for onesaram in allstudents:
    childs = onesaram.getchildren()
    sublist=[]
    for onedata in childs:
        sublist.append(onedata.text)
    total =float(sublist[1]+float(sublist[2])+float(sublist))

