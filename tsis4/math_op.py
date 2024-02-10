import math

degree = float(input('Input degree: '))
print(math.radians(degree))

height = float(input('Height: '))
a = float(input('Base, first value: '))
b = float(input('Base, second value: '))
print(((a+b)/2) * height)

sides = int(input('Input number of sides: '))
l = float(input('Input legnth of side: '))
print((1 / 4) * sides * l ** 2 * math.tan(math.pi / sides))

h = int(input('Height: '))
base = int(input('Base: '))
print(h*base)
