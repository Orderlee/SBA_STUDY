import numpy as np

data = np.array([[10,20],[30,40]])
print(data)
print('-'*20)

# 모든 요소의 합을 구함
result = np.sum(data)
print(result)
print('-'*20)

# 행을 따라가면서, 합을 실행
result = np.sum(data,axis=0) # 0 :  행 방향으로 덧
print(result)
print('-'*20)

result = np.sum(data, axis=1) # 1 : 열 방향으로 덧셈
print(result)
print('-'*20)

result = np.mean(data)
print(result)
print('-'*20)

result = np.min(data)
print(result)
print('-'*20)

result = np.max(data)
print(result)
print('-'*20)

result = np.max(data,axis=0)
print(result)
print('-'*20)
