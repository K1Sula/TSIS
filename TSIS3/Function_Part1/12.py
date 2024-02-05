n = int(input())
list1 = []
for i in range(n):
    x = int(input())
    list1.append(x)

def histogram(list1):
    for i in list1:
        for j in range(i):
            print("*" , end ='')
        print()
            
histogram(list1)