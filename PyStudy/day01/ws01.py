# 2개의 숫자를 입력받는다.
# 숫자가 아니면 다시 입력하라고 하고
# 프로그램 종료
# 두 개의 숫자의 합과 평균을 구하시오

# #solution 1.
#
# i1 = input("숫자를 입력하세요 : ")
#
# i2 = input("숫자를 입력하세요 : ")
#
# i3 = input("숫자를 입력하세요 : ")
#
# try:
#
#     int_i1 = int(i1)
#
#     int_i2 = int(i2)
#
#     int_i3 = int(i3)
#
# except:
#
#     print("숫자만 입력해주세요")
#
#     exit(1)
#
# sum = int_i1+int_i2+int_i3
#
# print("sum : ",sum," avg : ",round((sum)/3,2))

# #solution 2.
# i1 = input("숫자를 입력하세요 : ")
# i2 = input("숫자를 입력하세요 : ")
#
# if i1.isdigit() and i2.isdigit():
#     int_i1 = int(i1)
#     int_i2 = int(i2)
#     print("sum : ",int_i1+int_i2," avg : ",(int_i1+int_i2)/2)
# else :
#     print("숫자만 입력해주세요")

#solution 2.

# i1 = input("숫자를 입력하세요 : ")
#
# i2 = input("숫자를 입력하세요 : ")
#
# i3 = input("숫자를 입력하세요 : ")
#
#
#
# if i1.isdigit() and i2.isdigit():
#
#      int_i1 = int(i1)
#
#      int_i2 = int(i2)
#
#      int_i3 = int(i3)
#
#      print("sum : ",int_i1+int_i2+int_i3," avg : ",round((int_i1+int_i2+int_i3)/3,2))
#
# else :
#
#      print("숫자만 입력해주세요")

i1 = input("숫자를 입력하세요 : ")

i2 = input("숫자를 입력하세요 : ")

i3 = input("숫자를 입력하세요 : ")

sum = 0

try:

     int_i1 = int(i1)

     int_i2 = int(i2)

     int_i3 = int(i3)

     sum = int_i1+int_i2+int_i3

except:

     print("숫자만 입력해주세요")

     exit(1)

print("sum : ",sum," avg : ",round((sum)/3,1))