poli= input("Write string: ")

def check_is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    s_second = ''.join(reversed(s))
    return s == s_second
#string doesn`t have reverse function only in list so we use with join
if check_is_palindrome(poli):
    print("Yes")
else:
    print("No")

print(poli[::-1])