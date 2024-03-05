list = []

for i in range(1,11):
    x = input(f"{i} element: ")
    list.append(x)
new_tuple = tuple(list)
print(all(new_tuple))

# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true