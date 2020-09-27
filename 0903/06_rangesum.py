# 정수 2개를 입력 받아서, 앞수에서 뒷수 사이에 있는 모든 정수의 합을 구하세요.
# 앞수:2 뒷수:4 이면 2+3+4=9 출력
# 앞수:5 뒷수:2 이면 5+4+3+2=14 출력
# 출력예시: 2부터 4까지의 총합은 9 입니다.
# 만약 절대값 처리가 필요하면 abs 함수 사
first_number = abs(int(input('첫번째 숫자 입력하세요.: '))) #앞수
second_number = abs(int(input('두번째 숫자 입력하세요.: '))) #뒷수

if first_number > second_number :
    first_number, second_number = second_number,first_number

total= 0

for idx in range(first_number,second_number+1):
    total += idx

print('%d부터 %d까지의 총합은 %d 입니다.' % (first_number,second_number,total))



