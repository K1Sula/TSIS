def genpermutations(spaces, word):
    if len(word) == 0:
        print(spaces)
    else:
        for i in range(len(word)):
            new_s = spaces + word[i]
            new_w = word[:i] + word[i + 1:]
            genpermutations(new_s, new_w)

def ppermutations(s):
    genpermutations("", s)

string1 = input("Word: ")
print("After: ")
ppermutations(string1)


#learn more about this