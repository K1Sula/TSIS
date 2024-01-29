thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

for x in thisdict:
    print(x)


for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)