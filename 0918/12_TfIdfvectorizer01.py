from sklearn.feature_extraction.text import TfidfVectorizer

# TfidfVectorizer : 모든 문서에
# Tfidf = TF *IDF
vectorizer = TfidfVectorizer(min_df=1, stop_words=['친구'])

sentences = ['우리 아버지 여자 친구 이름은 홍길동 홍길동','홍길동 여자 친구 이름은 심순애 심순애','여자 친구 있나요.']

mat = vectorizer.fit(sentences)

print('단어 사전')
print(mat.vocabulary_)

print(vectorizer.get_feature_names())
print('-'*30)

myword = [sentences[2]]
print('myword:',myword)
print('-'*30
      )
print(vectorizer.get_stop_words())
print('-'*30)

print(vectorizer.get_feature_names())
print('-'*30)

print(vectorizer.get_feature_names())
print('-'*30)
print('끝')