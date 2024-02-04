strting1 = str(input())
list1 = strting1.split()

def reversestr(*list1):
    list2 = []
    for i in range(len(list1)):
        index = len(list1) - i - 1
        list2.append(list1[index])
    return list2
list2 = reversestr(*list1)
list3 = ' '.join(list2) # соединяет листы вместе = string
print(list3)