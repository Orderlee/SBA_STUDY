kim = ['김유신',10,20]
lee =['이순신',30,40]
park= ['박영희',60,50]
student = [kim,lee,park]

print(student)
print('-'*20)

mylist=list()

for sublist in student:
    mylist.append([sublist[0],sublist[1]+sublist[2]])
print(mylist)
print('-'*20)