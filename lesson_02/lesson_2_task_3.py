import math


def square(side):
    area = side * side
    return math.ceil(area)


square_side = 3.5
result = square(square_side)

print(f"Сторона квадрата: {square_side}, Площадь: {result}")
