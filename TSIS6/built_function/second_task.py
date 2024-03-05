string_1 = input("Write string: ")

def check_count(str1):
    count_for_upper = 0
    count_for_lower = 0
    for i in str1:
        char = i
        if char.isupper():
            count_for_upper += 1
        elif char.islower():
            count_for_lower += 1
    print("Number of lower case: ", count_for_lower)
    print("Number of upper case: ", count_for_upper)

check_count(string_1)
