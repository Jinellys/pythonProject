class Means_Of_Transport:
    'для определения цвета и марки машины'

    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def show_brand(self):
        print('марки транспортного средства', self.__brand)

    def show_color(self):
        print('цвет транспортного средства', self.__color)

    def set_bc(self, brand, color):
        self.__brand = brand
        self.__color = color

    def get_bc(self):
        return self.__brand, self.__color


class Car(Means_Of_Transport):
    car_drive = 4

    @classmethod
    def print_car_drive(cls):
        print(cls.car_drive)

    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels
        self.size = 4
        self._doors = 7
        self.__mass = 9

    def __str__(self):
        return f'Car: \n Brand - {self.get_bc()[0]}\n Color - {self.get_bc()[1]}\n Wheels - {self.wheels}'

    def __eq__(self, other):
        other_car_wheels = other.wheels if isinstance(other, Car) else None
        return self.wheels == other_car_wheels

    def __del__(self, wheels):
        pass

    def get_mass(self):
        return self.__mass


class Moped(Means_Of_Transport):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    @staticmethod
    def time_moped(max_speed, distance):
        return max_speed / distance


car = Car('BMW', 'red', 4)
car2 = Car('BMWqqq', 'redqqq', 3)
men = Means_Of_Transport('crfr', 'rvrf')
print(car.get_mass())
print(car)
print(car == men)
print(car._doors)
Car.print_car_drive()
#Means_Of_Transport.__doc__ ??????
