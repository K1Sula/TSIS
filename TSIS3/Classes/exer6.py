checklist = []

def is_prime(x):
    if x < 2:
        return False
    for i in range (2, int(x ** 0.5)  + 1):
        if x % i == 0:
            return False
    return True

for i in range (10):
    x = int(input())
    checklist.append(x)
print(f"All number {checklist}\n")

new_checklist = list(filter(lambda z : is_prime(z), checklist))

print(f"Prime numbers {new_checklist}")

#filter (function or none, iretable) -> true filter object
#lambda arguments : expression 
#map(function or None, *iretable) -> true filter object