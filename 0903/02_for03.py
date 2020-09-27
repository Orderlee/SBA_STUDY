examdata = [90,30,65,45,80]
print(examdata)

#원소 형태
for item in examdata:
    print(item)
print('-'*25)

#점수가 60이상이면 합격 그렇지 않으면 불합격으로 처리하기
#인덱스 형태(숫자)
for idx in range(len(examdata)):
    # idx는 0부터 4까지 가능
    #print(examdata[idx]) #인덱싱
    if examdata[idx] >= 60:
        print('{}번째 응시자 {}점 합격'.format(idx+1,examdata[idx]))
    else:
        print('{}번째 응시자 {}점 불합격'.format(idx+1,examdata[idx]))



print('-'*25)

print('합격자만 출력하기')

for idx in range(len(examdata)):
    if examdata[idx] >= 60:
        print('{}번째 응시자 {}점 합격'.format(idx+1,examdata[idx]))

    else:
        continue
        # continue 구문: 반복문을 사용하다가 continue를 만나면 이후 구문은 실행안되고
        # 다음 step으로 이동하기 위한 구문

print('-'*25)