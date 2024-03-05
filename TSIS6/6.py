import os
#d:\programming\educode\\tsis6\creator_files
directory = input("Write a path where you wanna creat: ")

if not os.path.exists(directory):
    os.makedirs(directory)# creat directories

list_of_char = []

for i in range(65, 91):
    x = chr(i)
    list_of_char.append(x)
    
for i in list_of_char:
    text_file = os.path.join(directory, f"{i}.txt")
    creator = open(text_file, "w")
    creator.write(f"This is file for {i}")
    creator.close()