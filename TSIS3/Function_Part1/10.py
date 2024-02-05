n = int(input())
list1 = []

for i in range(n):
    x = int(input())
    list1.append(x)
    
def dub(list1):
    i = 0
    while i < len(list1):
        j = i + 1
        while j < len(list1):
            if list1[i] == list1[j]:
                list1.pop(j)
            else:
                j += 1 
        i += 1                 
dub(list1)
print(list1)