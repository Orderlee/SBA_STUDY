# +=* 기호들을 연산자
# 변수 su는 연산의 대상이 되는 (피연산자)
su = 2+ 3 * 5
print(su)

su=(2+3) *5
print(su)

# =는 대입 연산자(우선 순위가 꼴찌)

# 비교(관계) 연산자: > >= < <= == !=
# 연산의 결과물은 반드시 True 또는 False가 된다
# 제어문 (if, for 구문 등등)에서 많이 사용되므로 중요!!
a=10
b=20

result = a>=b
print(result)

result = a<b
print(result)

result = a==b
print(result)

result = a!=b
print(result)

# 논리 연산자: and, or, not
a=10
b=20

first = a>= b #false
second = a!=b #true

result = first and second #false and true
print('논리연산자:',result)

# 연산자 우선 순위 : (),* 또는 / ,+ 또는 -, 관계 연산, not, and, or

third= a==b # false
result = first and second or third
print('논리연산자2:',result)

result =not(result) #진위값 반전
print('논리연산자3:',result)

