import time
import datetime



print(time.time())

localtime = time.localtime()
localtime2 = datetime.datetime.now()
print(localtime.tm_year)
print(localtime2)
print(type(localtime))
print(type(localtime2))