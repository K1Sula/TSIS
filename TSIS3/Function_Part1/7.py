n = int(input())
has_33 = []

for i in range(n):
    x = int(input())
    has_33.append(x)

def where_3(*has_33):
    Yes_3 = False
    for j in range(len(has_33)):
        if j == 0:
            if has_33[j] == 3 and has_33[j + 1] == 3:
                Yes_3 = True
                break
        elif j == len(has_33) - 1:
            if has_33[j] == 3 and has_33[j - 1] == 3:
                Yes_3 = True
                break
        elif has_33[j] == 3 and (has_33[j - 1] == 3 or has_33[j + 1] == 3):
            Yes_3 = True
            break

    return Yes_3

Which_one = where_3(*has_33)
print(Which_one)

