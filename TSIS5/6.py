import re
with open('row.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

answer = re.sub(r'[ ,.]', ':' , text)

print(answer)