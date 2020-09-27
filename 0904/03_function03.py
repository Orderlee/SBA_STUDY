# 두정수의 합을 구해주는 함수를 구현하고 테스트
# add(5,6)->11
# add(100,200)->300

def add_args(arg1,arg2):
    #print(arg1+arg2)
    return arg1+arg2

print(add_args(5,6))
print(add_args(100,200))

su1=5
su2=6
result=add_args(su1,su2)
print('결과:{}'.format(result))

su1=100
su2=200
result=add_args(su1,su2)
print('결과:{}'.format(result))


