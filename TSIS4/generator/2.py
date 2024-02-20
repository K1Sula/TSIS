def even(n):
    x = 0
    while x <= n:
        if x % 2 == 0:
            yield x
        x += 1


n = int(input())
EveN = even(n)

# print("First type of print : ")
# for i in EveN:
#     if i != n and i != n - 1:
#         print(i, end =", ")
#     else:
#         print(i)

print("Second type of print : ")
y = [i for i in EveN]
print(y)