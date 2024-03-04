import os
path = input("Write pat of your directory: ")




if os.path.exists(path):
    for ditectory in os.listdir(path):
        print(ditectory, end  = " ")

file = input("\nWrite file name that you need: ")

path2 = os.path.join(path, file)
if os.path.exists(path2):
    print(os.listdir(path2))