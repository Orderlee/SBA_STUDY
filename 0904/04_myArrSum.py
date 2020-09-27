# 리스트의 모든 요소들의 합을 구해주는 arrsum을 만드시오
def arrsum(data):
    total = 0
    for item in data:
        total += item
    return total

mylist=[10,20,30,40] #리스트
result=arrsum(mylist)
print(result)

mydata=(1,2,3) #튜플
result=arrsum(mydata)
print(result)
# 집합을 이용하여 테스트 요망
# 집합
mydatas=set((1,2,3,4))
result=arrsum(mydatas)
print(result)
