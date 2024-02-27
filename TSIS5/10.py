import re
string = '''Когото, писатель, оставался загадочной фигурой в мире литературы. 
Его творчество оставалось загадкой для многих, и его личность окутывалась тайной.
Многие пытались разгадать его мысли, исследовать его произведения, но никто не мог сказать 
наверняка, кто он был и что он думал. Его работы были полны загадок и символов, которые вызывали 
воображение и заставляли читателей задумываться. Некоторые считали его гением, другие - безумцем.
Он был как загадочный прохожий в ночи, оставляющий за собой следы загадочных мыслей и эмоций, 
которые продолжали жить в сердцах тех, кто встречал его творчество.'''

print('Original text')
print(string)
print()

def reveRse(string):
    words = re.findall(r'\b\w+\b' , string)
    string1 = ""
    for word in words:
        pattern = r'\b([a-zA-Z])|\b([а-яА-Я])'
        if re.search(pattern, word):
            ex =""
            s1 = word[0].upper()
            ex += s1
            s2 = word[1:].lower()
            ex += s2
            string1 += ex
        else:
            word = word.lower()
            string1 += word
    return string1
print('FOR camel case!')
print(reveRse(string))
print()
camel_case = (reveRse(string))


print('FOR snake case!')
def snake_case(str1):
    text1 = re.sub(r'(?<!^)([A-ZА-Я])', r'_\1',str1).lower()
    print(text1)

snake_case(camel_case)