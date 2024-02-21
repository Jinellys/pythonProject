class Calculator:

    # def __init__(self, num1):
    #     if num1 == int(num1):
    #     #if not insinstance(num1, int):
    #         self.num1 = num1
    #     else:
    #         raise TypeError('TypeError')
    #
    # def  __add__(self, num2):
    #     return Calculator(self.num1 + num2.num1)

    def calculate(self, a, b):
        if isinstance(a, (float, int)):
            if isinstance(b, (float, int)):
                return a + b
            else:
                raise TypeError('TypeError')

class Conc(Calculator):

    # def  __str__(self, num2):
    #      return Calculator(self.num1 + num2.num1)

    def calculate(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return f'{a}{b}'
        else:
            raise TypeError('TypeError')


# calc1 = Calculator(7)
# calc2 = Calculator(11)
# print(calc1.num1)
# calc1.num1 = 33
# print(calc1.num1)

calc = Calculator()
calc2 = Conc()
print(calc.calculate(25, 54))
print(calc2.calculate(str(25), str(54)))
