# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def say(self):
#         pass
#
#     def __init__(self, age: int, size: str):
#         self.__age = age
#         self.__size = size
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age / 2
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         self.__size = size
#
#
# class Cat(Animal):
#
#     @staticmethod
#     def prn(s):
#         print('This is static method))))')
#         c = Cat(10, 'bbb')
#         print(c.say())
#
#     # def __init__(self, age, size):
#     #     super().__init__(age, size)
#     def say(self):
#         print('cat say MAO')
#
#
# class Panda(Animal):
#
#     # def __init__(self, age, size):
#     #     super().__init__(age, size)
#     def say(self):
#         print('panda say RRRRRR')
#
#
# # animal = Animal(30, 'big')
# # print(animal.get_age())
# # animal.set_age(15)
# # print(animal.get_age())
# # print(animal.size)
# # animal.size = 'smoll'
# # print(animal.size)
#
#
# Cat.prn('BCFDXFZ')
# cat = Cat(24, 'middle')
# print(cat.get_age())
# print(cat.size)
# print(cat.say())
# animal = Cat(24, 'middle')
# animal2 = Panda(12, 'Big')
#
#
#
# animal.say()
# animal2.say()
# print(type(animal2))

class PC:
    def __init__(self, gpu_name='guyg', gpu_ram=50, gpu2_name='hgfhgfhg', gpu2_ram=88):
        self.gpu1 = GPU(gpu_name, gpu_ram)
        self.gpu2 = GPU(gpu2_name, gpu2_ram)

class GPU:
    def __init__(self, name, ram):
        self.name = name
        self.ram = ram

class PC_1:
    def __init__(self, gp :GPU):
        self.gpu1 = gp

my_PC = PC(gpu2_name='Eugenia')
print(my_PC.gpu1.name)
print(my_PC.gpu2.name)

gpu3 = GPU('nbnb', 22)
print(gpu3.name)
pc1 = PC_1(gpu3)
print(pc1.gpu1.name, pc1.gpu1.ram)