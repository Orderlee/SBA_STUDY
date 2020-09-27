tuple01=('김철수',40,50,60)
tuple02=('박명희',50,60,70)

mytuple=(tuple01,tuple02)
print(mytuple)

print('총 인원수:', len(mytuple),'명',sep='')

saram=mytuple[0][0]
score=mytuple[0][1:]
print(saram)
print(score)

hap=sum(score)
print(hap)
mylen=len(score)
avg=hap/mylen
print('이름: ',saram,', 평균: ',avg,'점', sep='')

print('-'*30)

# 국어의 평균
print('국어의 평균')
kor = mytuple[0][1]+mytuple[1][1]
mylen=len(mytuple)
print(kor/mylen)