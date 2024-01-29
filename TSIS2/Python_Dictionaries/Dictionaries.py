thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Dictionaries are used to store data values in key:value pairs.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

# Dictionary items are ordered, changeable, and does not allow duplicates!!!.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway") #one round-brackets
print(thisdict)