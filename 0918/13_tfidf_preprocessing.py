import pandas as pd
DATA_IN_PATH = '../data_in/'
TRAIN_CLEAN_DATA = 'train_clean.csv'

train_data = pd.read_csv(DATA_IN_PATH + TRAIN_CLEAN_DATA)
print(train_data.info())
print('-'*30)

print(train_data.columns)
print('-'*30)

print(train_data['sentiment'].unique())
print('-'*30)

myseris = train_data.groupby('sentiment')['sentiment']
result = myseris.count()
print(result)

# 리뷰와 정답 데이터를 리스트화
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

from sklearn.feature_extraction.text import TfidfVectorizer

# analyzer : word, char
# max_features : 최대 길이
# ngram_range : very good
vectorizer = TfidfVectorizer(min_df = 0.0, analyzer='char', max_features=5000, ngram_range=(1,3))

import numpy as np

x = vectorizer.fit_transform((reviews))
y = np.array(sentiments)

#print('x:\n',x)
#print('-'*30)

features = vectorizer.get_feature_names()
print('토큰갯수 :',len(features))
print('토큰화된 단어 리스트 :',features)

from sklearn.model_selection import train_test_split
seed=2
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=seed)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight='balanced')

model.fit(x_train,y_train)

predicted = model.predict(x_test,y_test)

print('정확도 : %.4f' % model.score(x_test))

TEST_CLEAN_DATA = 'test_clean.csv'

test_data = pd.read_csv(DATA_IN_PATH + TEST_CLEAN_DATA)
testDataVec = vectorizer.transform(test_data['review'])

test_predicted = model.predict(testDataVec)
print('test_predicted:', test_predicted)

import os

DATA_OUT_PATH = '../data_out'

if not os.path.exists(DATA_OUT_PATH):
    os.makedirs(DATA_OUT_PATH)

myframe = pd.DataFrame({'id':test_data['id'], 'sentiment':test_predicted})
saved_file_name='model_tfidf_answer.csv'
myframe.to_csv(DATA_OUT_PATH + saved_file_name,index=False, quoting=3)
print(saved_file_name +' 파일 저장되었습니다.')

print('끝')
