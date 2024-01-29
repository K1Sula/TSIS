
fruits = {"apple", "banana", "cherry"}
if "apple"  in fruits:
  print("Yes, apple is a fruit!")
  
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


fruits.remove("banana")
fruits.discard("banana")