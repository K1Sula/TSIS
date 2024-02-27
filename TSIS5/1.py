import re

def searchWord(text):
    words = text.split()
    for word in words:
        if re.search(r'а(?:б*)', word):  
            print(word, end = " ")

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read() 

searchWord(text)
