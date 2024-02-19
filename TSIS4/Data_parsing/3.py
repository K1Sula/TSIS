import datetime

now = datetime.datetime.now()

#function to drop microsecond
stripped_time = now.replace(microsecond=0)

print("Original:", now)
print("Stripped:", stripped_time)
