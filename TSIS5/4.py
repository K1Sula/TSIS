import re
with open('row.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

def Upc(text):
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if re.search(r'([A-Z]|[А-Я])([a-z]|[а-я])+', word):
            print(word , end = " ")

Upc(text)