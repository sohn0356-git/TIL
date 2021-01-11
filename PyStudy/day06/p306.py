# try:
#     f = open("live.txt","rt")
#     text = ""
#     line = 1
#     while True:
#         row = f.readline()
#         if not row:
#             break
#         text += str(line) + " : " + row
#         line += 1
#     print(text)
# except FileNotFoundError:
#     print("There isn't file")
# finally:
#     f.close()


try:
    f = open("live.txt","rt", encoding='UTF-8')
    rows = f.readlines()
    for row in rows:
        print(row, end = '')
except FileNotFoundError:
    print("There isn't file")
finally:
    f.close()