def squar(n):
    x = 1
    while x ** 2 <= n:
        yield x ** 2
        x += 1

N = int(input("Enter a number: "))
s = squar(N)

for i in s:
    print(i, end = " ")


"""
Генератор в Python - это функция, которая использует ключевое слово yield 
для производства последовательности значений на лету. 
Каждый раз, когда генератор встречает оператор yield, он возвращает значение, 
указанное после yield, но сохраняет свое состояние, чтобы продолжить выполнение 
с того же места при следующем вызове.  Это позволяет генераторам создавать итерируемые
последовательности без необходимости хранить все значения в памяти одновременно.
"""

# нагыз генератор 
# class Iter:
#     def __init__(self,n):
#         self.n = n
#         self.i = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.i * self.i <= self.n:
#             result = self.i ** 2
#             self.i += 1
#             return result
#         else:
#             raise StopIteration
        
# N = int(input())

# itEr = Iter(N)


# for i in itEr:
#     print(i , end = " ")

# тагы быр жол (нешеу болып кетты Кудай-ай)


# def squar(n, x=1):
#     if x ** 2 <= n:
#         yield x ** 2
#         yield from squar(n, x + 1)

# N = int(input("Введите число: "))
# s = squar(N)

# for i in s:
#     print(i, end=" ")