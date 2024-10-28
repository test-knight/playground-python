import math


def calculate_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Input must be a numeric value")

    area = math.pi * radius**2
    return area

try:
    print("Area with radius 5: ", calculate_area(5))
except ValueError as e:
    print(e)

try:
    print("Area with radius 2.5: ", calculate_area(2.5))
except ValueError as e:
    print(e)

try:
    print("Area with radius 'abc': ", calculate_area('abc'))
except ValueError as e:
    print(e)


try:
    print("Area with radius None: ", calculate_area(None))
except ValueError as e:
    print(e)