f = open("live.txt", "wt", encoding='UTF-8')
f.write("""God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his side
With love & strength for each new day
He will make a way
He will make a way
God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his side
With love & strength for each new day
He will make a way
He will make a way
By a roadway in the wilderness
He'll lead me
Rivers in the desert
Will I see
Heaven & earth will fade
But his word will still remain
& He will do something new today
God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his…""")
print(type(f))
f.close()
fr = None
try:
    fr = open("liv.txt","rt", encoding="UTF-8")
    text = fr.read()
    print(text)
except FileNotFoundError:
    print("There isn't file")
finally:
    if fr != None:
        fr.close()
# try:
#     f2 = open("live.txt","rt")
#     while True:
#         text = f2.read(10)
#         if len(text)==0:
#             break
#         print(text, end = '')
# except FileNotFoundError:
#     print("There isn't file")
# finally:
#     f2.close()