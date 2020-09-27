# 100번 반복.
# 매번 1부터 10사이의 임의의 수를 추출한다. (random 모듈)
# 이것을 사전에 담고, 최종결과를 출력하도록 한다. ('1':2, '2':5...)
# list comprehension을 사용 하여 리스트로 만든 다음 mylist.sort() 함수를 사용하여 정렬
# 출력결과 예시
# 숫자 1은 12번 추출
# 숫자 2는 5번 추출
# ...
# 숫자 10은 4번 추출

import random
count_dict=dict() #empty dict
for idx in range(1,101):
    data = random.randint(1,10)

    if data in count_dict:
        count_dict[data] += 1
    else:
        count_dict[data] = 1


print(count_dict)


count_list=[key for key in count_dict.keys()]
count_list.sort()

for key in count_list:
    print('숫자 %d는 %d번 추출' % (key,count_dict[key]))

print(count_list)
