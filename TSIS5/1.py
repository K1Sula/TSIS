import re


# \A - this for start with string like that
# \b - this mean that into string we have word and into this word need start with this

#  Example: "The PP2  interesting and we like learn"
#  if we write print(r'\AThe') output: 
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
answer1 = re.findall(r'а(?:б*)', text)
print("Answer for 1 task => " , answer1)

answer2 = re.findall(r'аб{2,3}(?![б])', text)
print('\n', "Answer for 2 task => " , answer2)



