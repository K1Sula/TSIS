fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)
print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)
print()
for x in range(2, 6):
    print(x)

print()
for x in range(
    2, 30, 3
):  # 2 is start ; 30 is finish ; (i + 3) that mean 3 is increment
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print()
for x in range(6):
    if x == 3:
        break  # this break stop ALL LOOP
    print(x)
else:
    print("Finally finished!")

print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    print('\n') #print endl -> end line
    for y in fruits:
        print(x, y , end = " ") # print on in one row
        
        
#for loops cannot be empty, but if you for some 
# reason have a for loop with no content, put in the
# pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass