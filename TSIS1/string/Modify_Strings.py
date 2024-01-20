a = "Hello, World!"
print (a.upper()) #HELLO, WORLD!
print (a.lower()) #hello, world!

#whitespce before and after any string isn`t  needed so we can remote this
b = "    Hello, World!    "
print (b.strip()) #Hello, World!

c = "Hello, World!"
print(c.replace("H", "J")) #Jello, World!



a = "Hello, World!"
'''
The split() method returns a 
list where the text between 
the specified separator becomes the list items.
'''
print(a.split(",")) # returns ['Hello', ' World!']