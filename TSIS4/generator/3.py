def cheak(n):
    x = 0
    while x <= n:
        if x % 3 == 0 and x % 4 == 0:
            yield x 
        x += 1


n = int(input())
y = cheak(n)
for i in y:
    print(i, end = " ")