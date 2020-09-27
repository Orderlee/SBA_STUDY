#학생의 이름과 국어, 영어, 수학 점수를 입력 받으세요
#김철수 50, 60, 80
#총점은 소수점 2자리로 평균은소수점 3자리로 출력 하세요.
#출력결과
#이름: 김철수
#국어: 50점
#영어: 60점
#수학: 80점
#총점: 190.00
#평균: 63.333


# print('이름을 입력:')
# name = input()
# age = input('나이 입력:')
# print('이름:',name,'나이:',age)
#
# #데이터 형변환: 바뀔타입(바꿀데이터)
# # int는 정수형, str은 문자열형
# newage = int(age) +5
print('이름:')

name=input()
kor = int(input('국어 점수:'))
eng = int(input('영어 점수:'))
math = int(input('수학 점수:'))
total = kor+eng+math
avg = total/3.0
print('이름:%s ' % name)
print('국어: %d점' %kor)
print('영어: %d점' %eng)
print('수학: %d점' %math)
print('총점:%7.2f점'% total)
print('평균:%6.2f점' % avg )
