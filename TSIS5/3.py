import re

with open('row.txt', 'r' , encoding="utf-8") as file:
    text = file.read()

def check(text):
    words = re.findall(r'\b\w+\b' , text)
    for word in words:
        if re.search(r'\b[а-яА-Я]+_[а-яА-Я]+\b', word):
            print(word)

check(text)