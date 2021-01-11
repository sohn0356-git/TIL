f = None
f = open("live.txt", "rt",encoding="UTF-8")
f.seek(-5,2)
text = f.read(1)
print(text)

ff = None
ff = open('text.txt','rt', encoding='UTF-8')
ff.seek(7,0)
text = ff.read()
print(text)