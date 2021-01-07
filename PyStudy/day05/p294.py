d = 0
result = 0
try:
    num = int(d)
    result=10/num
except ValueError as e:
    print(e.with_traceback())
    print("invalid data")
    exit()
except ZeroDivisionError as e:
    print(e.with_traceback())
    print("Zero Division")
    exit()

print(result)