import json

filename='../attach2/some.json'

myfile = open(filename, 'rt', encoding='utf-8')
print(type(myfile))
myfiles =myfile.read()
print(type(myfiles))

#json_str =json.dumps(myfile, ensure_ascii=False, indent=4, sort_keys=True)
json_Data=json.loads(myfiles)
print(json_Data)
print(type(json_Data))
#print(json_str)

print('이름:',json_Data['member']['name'])
print('주소:',json_Data['member']['address'])
print('전화번호:',json_Data['member']['phone'])
print('카페주소:',json_Data['web']['cafename'])
print('아이디:',json_Data['web']['id'])