# 계산기
# 계산기 A: 3+4=7
# 계산기 B: 5+15=20

# step1 : 클래스(템플릿) 정의
# step2 : 객체 생성
# step3 : 변수에 값을 할당하거나, 메소드 호출 등을 사용함
# step4 : 출력이나 다른 용도로 사용

# 클래스 구성 요소: 변수, 함수, 생성자(__init__)
# 생성자 : 내부에 들어 있는 변수들의 초기화 용도로 사용
#        한 번만 호출이 되는 특수한 메소

# self 키워드 : 호출되고 있는 객체의 정보가 복사되는 변수
class Calulator: #step1 클래스 정의
    def __init__(self,data):
        self.result = 0 # 총합을 0으로 초기
        self.data = data
        print(self.data + ' 계산기가 생성되었습니다.')
        print('계산기 초기값 :',self.result)

    def calc(self, num): # 함수는 동작
        self.result += num
        return self.result

# step2 객체 생성 : 해당 클래스를 이용하여 물건 생성
# calulator는 생성자가 되고,
# 규칙 : 생성자의 이름은 클래스의 이름과 동일 해야한다.
# step2
cal1 = Calulator('계산기 A')
# step3
print(cal1.calc(3))
print(cal1.calc(4))
print(cal1.calc(4))
print('-'*30)


cal2 = Calulator('계산기 B')
print(cal2.calc(5))
print(cal2.calc(15))
print('-'*30)
print('finished')