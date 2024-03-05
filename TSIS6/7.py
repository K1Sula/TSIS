
try:
    with open("einstein.txt", 'r') as file:
        f = file.read()
except FileNotFoundError:
    print("This file doesn`t exist")
#append - 'a'
x = input("Write name text file: ") + ".txt"
creator = open(x,  'a')
creator.write(f)

reader = open(x, 'r')
f = reader.read()
print(f)