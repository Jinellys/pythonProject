from random import randint
a = randint(1,10)

while True:
    b = int(input('Vvedite chislo'))
    if b > a:
        print('Vashe Chislo bolshe')
    elif b < a:
        print('Vashe chislo menshe')
    else:
        print('You cool!')
        break
