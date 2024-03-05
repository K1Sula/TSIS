x = input("Write file name: ")

x = x + ".txt"
#create
f1 = open(x, 'x')
list_ex = [i for i in range(10)]
#here we also have writelines() Method
#write
for i in list_ex:
    with open(x, 'w') as file:
        for item in list_ex:
            file.write(str(item) + ' added new' +'\n') 

#read
with open(x, 'r') as file:
    f = file.read()

print(f)