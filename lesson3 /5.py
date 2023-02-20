import time
import datetime
x = datetime.datetime(2023, 8, 13).timetuple()
y = time.mktime(x)

print(y)