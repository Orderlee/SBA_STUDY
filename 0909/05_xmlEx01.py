# xml 문서 규칙
# 최상위 엘리먼트는 반드시 1개이어야 함
# 1.대소문자를 구분한다
# 2.닫는 엘리먼트는 </엘리먼트이름>의 형식으로 작성
# 3.내용물이 없는 경우에는 <엘리먼트 이름 />으로 작성 가능
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

human = Element('human')
human.attrib['birth'] ='19701225'
human.attrib['gender'] = '남성'

SubElement(human, 'name').text ='홍길동'
SubElement(human,'age').text ='30'
SubElement(human, 'address').text =' 용산구 도원동'

def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(human)

xmlFile='xmlEx_01.xml'

ElementTree(human).write(xmlFile, encoding='utf-8')

print(xmlFile + '파일이 생성되었습니다.')


print('-'*40)
note = Element('note')
note.attrib['no']='100'

SubElement(note,'to').text = 'Tove'
SubElement(note, 'from').text = 'Jani'
SubElement(note, 'heading').text='Reminder'
SubElement(note, 'body').text="Don't forget me this weekend!"

def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)

xmlFile='note.xml'

ElementTree(note).write(xmlFile, encoding='utf-8')

print(xmlFile + '파일이 생성되었습니다.')