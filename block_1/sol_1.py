import math


# Дана сторона квадрата a. Найти его периметр P = 4·a
def perimetr(a: float):
    return a * 4


# Дана сторона квадрата a. Найти его площадь S = a2
def kvadrat(a: float):
    return a ** 2


# Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
def square(a: float, b: float):
    return a * b


def perimeter(a: float, b: float):
    return 2 * (a + b)


# side1, side2 = float(input()), float(input())
# print(square(side1, side2), perimeter(side1, side2))

# Дан диаметр окружности d. Найти ее длину L = π·d, π = 3.14

def circle(d: float):
    return d * math.pi


# Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2

def cube(a: float):
    v = a ** 3
    s = 6 * (a ** 2)
    return v, s


# c = list(cube(float(input())))
# print('объем куба V =', c[0],'\n''площадь его поверхности S =', c[1])

# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)


def paral_v(a: float, b: float, c: float):
    v = a * b * c
    return v


def paral_s(a: float, b: float, c: float):
    s = 2 * (a * b + b * c + a * c)
    return s


# a, b, c = float(input()), float(input()), float(input())


# Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14

def length_circle(r: float):
    return 2 * math.pi * r


def area_circle(r: float):
    return math.pi * (r ** 2)


# radius = float(input())
# print(length_circle(radius))
# print(area_circle(radius))

# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

def arithmetic(a: float, b: float):
    return (a + b) / 2


# Даны два неотрицательных числа a и b. Найти их среднее геометрическое,
# т. е. квадратный корень из их произведения: (a·b)1/2

def geom(a: float, b: float):
    return math.sqrt(a * b)


# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов

def summa(a2: float, b2: float):
    return a2 + b2


def difference(a2: float, b2: float):
    return a2 - b2


def composition(a2: float, b2: float):
    return a2 * b2


def private(a2: float, b2: float):
    return a2 / b2

# num1 = float(input())**2
# num2 = float(input())**2
# print(summa(num1, num2))
