import datetime

x = datetime.datetime.now()
y = x + datetime.timedelta(days = 1 )
z = x - datetime.timedelta(days = 1 )
print(z.strftime("Yesterday: %A"))
print(x.strftime("Today: %A"))
print(y.strftime("Tommorow: %A"))
