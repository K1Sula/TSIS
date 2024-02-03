x1 =  float(input("Enter first x coordinate number = "))
y1 =  float(input("Enter first y coordinate number = "))

x2 =  float(input("Enter second x coordinate number = "))
y2 =  float(input("Enter second y coordinate number = "))

class Point:
    def __init__(self, * , x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def show(self):
        print (f"first coordinates is [{self.x1},{self.y1}]")
        print (f"second coordinates is [{self.x2},{self.y2}]")
    
    def move(self):
        Q = str(input("""
If you want to change first coordinates write \'1\',
if you want to change second coordinates write \'2\',
if you want to change both coordinates write \'3\',
if you don't want to change, write \'0\'
"""))
        if Q == "1":
            self.x1 = input("x = ")
            self.y1 = input("y = ")
        elif Q == "2":
            self.x2 = input("x = ")
            self.y2 = input("y = ")
        elif Q == "3":
            self.x1 = input("Firts x = ")
            self.y1 = input("First y = ")
            self.x2 = input("Fecond x = ")
            self.y2 = input("Fecond y = ")
        else :
            pass
    def dist(self):
        formula = (self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2 
        return formula ** 0.5
    
Geometry = Point(x1 = x1 , y1 = y1, x2 = x2, y2 = y2)

Geometry.show()
Geometry.move()

print(Geometry.dist())