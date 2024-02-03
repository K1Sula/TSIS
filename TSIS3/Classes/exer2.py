x = int(input())
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
result1 = Shape()
print(result1.area1())
result2 = Square(x)
print(result2.area2())


