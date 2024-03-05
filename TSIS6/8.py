import os
import re


x1 = input("Write file name: ")
path_of_file = "D:\Programming" + f"\\{x1}" + '.txt'
try:
    if not os.path.exists(path_of_file):
        with open(path_of_file, 'x') as creat_file:
            c = creat_file.write("Hello, World!")
except FileNotFoundError:
    print("File created before")


#способы найти файлы 
#первый способ через regex
found1 = re.findall(r"\\([^\\]*\.txt)", path_of_file)
print(found1) #list
#D:\Programming\Educode\TSIS6\namefile.txt

# second type to find is os.path.basename()
found2 = os.path.basename(path_of_file)
print(found2) #simply print


#where file ?
def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

    return None

filename = f"{found2}"
search_path = "/"

result = find_file(filename, search_path)
if result:
    os.remove(path_of_file)
    print("File successfully deleted")
else:
    print("Файл не найден.")





# Поместив [^\\]*\.txt в скобки (), 
# мы указываем, что эта часть шаблона должна быть рассмотрена как захватывающая группа. 
# Это означает,что совпавшая подстрока (часть пути, содержащая имя файла с расширением .txt) 
# будет сохранена и может быть доступна
# отдельно от общего совпадения. Это полезно, когда вы хотите 
# извлечь определенные части совпадающего текста.