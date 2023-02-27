import datetime

x = datetime.datetime(2022, 5, 4)
while x.strftime("%a") != 'Mon':
    x -= datetime.timedelta(days=1)
x -= datetime.timedelta(days=5)
print(x)