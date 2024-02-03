x = int(input("Enter square lenght = "))
x1 = int(input("Enter regtangle lenght = "))
y1 = int(input("Enter regtangle width = "))

class Shape:
    def __init__(self):
        pass
    def area1(self):
        return 0
class Square(Shape):
    def __init__(self,lenght):
        super().__init__()
        self.lenght = lenght
    def area2(self):
        return self.lenght * self.lenght
class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__()
        self.lenght = lenght
        self.width = width
    def area3(self):
        return self.lenght * self.width


result1 = Shape()
print(result1.area1())

result2 = Square(x)
print(result2.area2())

result3 = Rectangle(x1,y1)
print(result3.area3())

