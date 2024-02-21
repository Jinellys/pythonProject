# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

a, b, c = map(int, input().split())
count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1
print(count)

# Даны два числа. Вывести большее из них

a, b = int(input()), int(input())
if a > b:
    print(a)
else:
    print(b)

# Даны два числа. Вывести вначале большее, а затем меньшее из них.

a, b = int(input()), int(input())
if a > b:
    print(a, b)
else:
    print(b, a)

# Даны три числа. Найти наименьшее из них

a, b, c = map(int, input().split())
print(min(a, b, c))

a, b, c = map(int, input().split())
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

# Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.

x, y = int(input()), int(input())
if x < 0 > y:
    print('номер координатной четверти - III')
elif x > 0 < y:
    print('номер координатной четверти - I')
elif x < 0 < y:
    print('номер координатной четверти - II')
else:
    print('номер координатной четверти - IV')





