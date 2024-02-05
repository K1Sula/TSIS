name = str(input())

def palindrome(name):
    i = 0
    while i < len(name) / 2 + 1:
        if name[i] != name [len(name) - i - 1]:
            return False
        i += 1
    return True
    
if palindrome(name) == True:
    print("Yes")
else: 
    print("No")