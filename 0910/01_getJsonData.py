# __name__: 파이썬이 내장하고 있는 내부 변수
# 애플리케이션 이름이 저장되어 있다.
# 해당 애플리케이션이 스스로 실행하면  '__main__' 값이 대입 됨

import json

def get_Json_Data():
    print('함수 호출 됨')
    filename = '../attach2/jumsu.json'

    myfile=open(filename,'rt',encoding='utf-8')
    print(type(myfile))

    myfile=myfile.read()
    print(type(myfile))
    # loads(str):문자열 형식의 데이터를 이용하여 json타입으로 변환해 주는 함수
    jsonData = json.loads(myfile)
    print(type(jsonData))
    print('-'*30)

    for oneitem in jsonData:
        print(oneitem.keys())
        print(oneitem.values())
        print('이름:',oneitem['name'])
        kor = float(oneitem['kor'])
        eng = float(oneitem['eng'])
        math = float(oneitem['math'])

        total = kor +eng +math
        print('총점:', total)

        if 'hello' in oneitem.keys():
            message = oneitem['hello']
            print('message:', message)

        _gender = oneitem['gender'].upper()

        if _gender =='M':
            gender ='남자'
            print('성별:', gender)
            #print('성별: 남자')
        elif _gender =='F':
            gender ='여자'
            print('성별:',gender)
            #print('성별: 여자')
        else:
            print('성별: 미정')

if __name__ == '__main_':
    print('스스로 실행되었습니다.')
    get_Json_Data() #함수 호출
else:
    print('다른 프로그램이 호출했습니다.')
