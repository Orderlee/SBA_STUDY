from sklearn.feature_extraction.text import CountVectorizer

# CountVectorizer : 문자열에서 단어 토큰을 생성하여 BOW로 인코 된 벡터를 생성해줌
# df : documnet-frequency
# min_df=2 : 최소빈도가 2번 이상인 단어들
# stop_words : 불용
vectorizer = CountVectorizer(min_df=1, stop_words=['친구'])
print(type(vectorizer))

sentences = ['우리 아버지 여자 친구 이름은 홍길동 홍길동','홍길동 여자 친구 이름은 심순애 심순애','여자 친구 있나요.']

# 단어사전
mat = vectorizer.fit(sentences)
print(type(mat))

print(mat.vocabulary_)
print(sorted(mat.vocabulary_.items()))

# 토큰
features = vectorizer.get_feature_names()
print(type(features))
print(features)

print('불용어')
print(vectorizer.get_stop_words())

myword =[sentences[0]]
print('myword :', myword)

myarary = vectorizer.transform(myword).toarray()
print(type(myarary))

'''
0('여자')이 1번, 1('이름은')
'''

print('myaray:' ,myarary)
print('finished')
