from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def voice(self):
        pass


class Cat(Animal):

    def voice(self):
        return 'MEOW'