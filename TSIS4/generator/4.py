def AtoB( * , a , b):
    for i in range(a , b):
        yield i ** 2
first = int(input())
second = int(input())

s = AtoB(a = first, b = second )
for i in s:
    print(i, end = " ")