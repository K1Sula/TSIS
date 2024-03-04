import os

def list_directories(path):
    directories = []
    for item in os.listdir(path): # output every file in this case
        full_path = os.path.join(path, item) 
        if os.path.isdir(full_path): #если вообще папки ищет
            directories.append(item)
    return directories

def list_files(path):
    files = []
    for item in os.listdir(path):
        full_path = os.path.join(path,item)
        if not os.path.isdir(full_path):
            files.append(item)
    return files

# os.path.join() - это функция в модуле os.path в Python,
# используемая для объединения одного или нескольких компонентов пути
# Например, если path равен "C:/Users/Username/Documents", 
# а item равен "folder", то os.path.join(path, item) вернет "C:/Users/Username/Documents/folder"


path = input("Write path of you need: ")
directories = list_directories(path)
files = list_files(path)
print("list of directories:")

for directory in directories:
    print(directory, end = " ")


print("\nlist of files:") 
for file in files:
    print(file, end = " ")

print("\nAll item: ")
print(os.listdir(path))