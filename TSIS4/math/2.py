import math

def areatr(*, Height, roof, floor):
    p = (roof + floor) / 2
    return p * Height 

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

print("Expected Output: ", areatr(floor = b, roof = a, Height = h) )