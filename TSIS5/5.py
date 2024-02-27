import re
with open('row.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

def Upc(text):
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if re.search(r'а\w*б\b', word):
            print(word , end = " ")

Upc(text)