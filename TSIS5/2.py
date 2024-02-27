import re

with open("row.txt", 'r', encoding="utf-8") as file:
    text = file.read()

# we create function
def find(text):
    words = re.findall(r'\b\w+\b', text) #do list
    for word in words:
        if re.search(r'а(б{2,3})', word) != None: #find one of them
            print(word)

find(text)

#code find only one time 
# match = re.search(r'а(б{2}|б{3})', text)

# if match:
#     answer = match.group()
#     print(answer)
# else:
#     print("Pattern not found in the text.")
