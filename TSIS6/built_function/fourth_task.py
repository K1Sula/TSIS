import time 
import math


# in 1 second we have 1000 miliseconds
x = int(input("Write number what you want Square root: "))
y = int(input("Write miliseconds: "))

result = math.sqrt(x)

time.sleep(y / 1000)
print(f"Square root of {x} after {y} miliseconds is ", result )