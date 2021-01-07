str1 = 'python';

print(str1[0])
print(str1[-3])
print(str1[-6])

for i in range(1,len(str1)+1):
    print(str1[-i],end=',')


print()
filename = '20210104-132400.jpg'

print(filename[:4]+"년 ",int(filename[4:6]),"월 ",int(filename[6:8]),"일",sep='')
hour = int(filename[9:11])
if hour>12:
    hour-=12
minute = filename[11:13]
sec = filename[13:15]
print(hour,"시 "+minute+"분 "+sec+"초")
print("파일 형식 "+filename[-3:])