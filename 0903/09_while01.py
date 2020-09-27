#1부터 10까지의 총합을 구하시오

total=0
i=1 #초기식
# while 조건식:
while i<11:
    total += i
    i+=1 #증감식

print('총합:%d' % total)

print('-'*30)
# 2+5+8+..50=442
total = 0
i=2

while i<51:
    total += i
    i+= 3

print('총합:%d' % total)

print('-'*30)
#1+3+5+..+97+99=2500

total = 0
i=1
while i<100:
    total+= i
    i+= 2
print('총합:%d' % total)

print('-'*30)



