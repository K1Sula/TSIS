x = "awesome" # <= this is global

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"

def myfunc1():
  x = "fantastic" # <= this is local
  print("Python is " + x)

myfunc1()

print("Python is " + x)