# Напишите программу для подсчета среднего числа всех введенных пользователям чисел.

def arithmetic_avg() -> float:
    a = int(input())
    count = 0
    summa = 0
    while a != 0:
        summa += a
        count += 1
        a = int(input())
    return summa / count


print(arithmetic_avg())

# Напишите программу для вывода на экран чисел от 0 до 100

print(*(i for i in range(0, 101)))

# Напишите программу для вывода таблицы умножения от 0 до 9.

for i in range(0, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

# Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте тоже самое со словарем и выведите ключ и значение)

sp = [25, 'bol', 4.5, 'a', 12]
print(*(i for i in sp), sep=', ')

my_dict = {'kitten': 4, 'cat': 12, 'puppy': 6, 'dog': 3}
for key, value in my_dict.items():
    print(key, value)
