import math

deg = float(input("Input degree: "))

def tran(deg):
    return deg * (math.pi / 180)

print("Output radian: " , tran(deg))