import numpy as np

print(np.zeros(3))

arr = np.zeros((2,2)) # (행,열)
print(arr)

arr2 =np.ones((3,2))
print(arr2)

# 연립 방벙식을 풀고자 할 때 사용(가우스 소거법)
# 크기가 3인 단위 행렬을 만들어 줌
# 정방 행렬: 행과 열의 크기가 같은 행
arr3= np.eye(3)
print(arr3)

# 모든 요소의 값이 5행 2행 2열의 행렬을 생성
arr4 = np.full((2,2),5)
print(arr4)
print('finished')