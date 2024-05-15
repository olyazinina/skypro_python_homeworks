from math import ceil


def square(a):
    s = a ** 2
    return s


a = float(input("Сторона квадрата: "))
result = ceil(square(a))
print(result)