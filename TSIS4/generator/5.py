class Iter:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n >= 0:
            res = self.n - 1
            return res
        else:
            raise StopIteration
        
Number = int(input())

result = Iter(Number)

for i in result:
    print(i, end = " ")