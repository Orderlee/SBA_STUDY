'''
당뇨병 정보를 저장한 파일을 7대3으로 나누어라
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

filename='../logisticexample/pima-indians-diabetes.csv'
data = pd.read_csv(filename)
print(data.columns)
print(data.shape)

print(data['class'].unique())

inputData =['pregnant', 'plasma', 'pressure', 'thickness', 'insulin', 'BMI',
       'pedigree', 'age']
x_data = [inputData]
y_data = ['class']

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.3)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

# 모델 생성하기






