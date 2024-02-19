def parallelogram_area(base, height):
    return base * height

base = float(input("Enter the length of the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = parallelogram_area(base, height)

print("The area of the parallelogram is:", area)
