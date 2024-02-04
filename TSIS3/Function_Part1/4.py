list1 = []
for i in range(7):
    z = int(input())
    list1.append(z)

def filter_prime(*list1):
    list2 = []
    for q in list1:
        if q < 2:
            continue
        is_prime = True
        for ai in range(2, int(q ** 0.5) + 1):
            if q % ai == 0:
                is_prime = False
                break
        if is_prime == True:
            list2.append(q)
    return list2

result = filter_prime(*list1)
print(result) 