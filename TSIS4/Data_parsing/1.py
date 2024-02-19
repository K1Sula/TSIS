import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))
for i in range(4):
    next_day = x + datetime.timedelta(days = i + 1)
    print(next_day.strftime("%A"))
