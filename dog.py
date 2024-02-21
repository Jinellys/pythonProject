class DogSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DogSingleton, cls).__new__(cls)
        else:
            print('We can not create another class.')
        return cls.__instance

    def __init__(self, size=None, color=None, mass=None, breed=None, group=None):
        self.size = size
        self.color = color
        self.mass = mass
        self.breed = breed
        self.group = group

    def __str__(self):
        return f'Dog:\nsize {self.size}\ncolor {self.color}\nmass {self.mass}\nbreed {self.breed}\ngroup {self.group}'

    def voice(self):
        print('quack-quack')

    def jump(self):
        print("I'm jumping")

    def run(self):
        print("I'm running")

    def Giving_a_paw(self):
        print('I give you a paw')

    # @staticmethod
    # def get_instance():
    #     if not DogSingleton.__instance__:
    #         DogSingleton()
    #     return DogSingleton.__instance__


dog = DogSingleton('big', 'black', 35, 'sheepdog', 'a service')
# dog = DogSingleton.get_instance()
# dog.mass = 30
print(dog)
# dog2 = DogSingleton()
# print(dog2)
# print(dog == dog2)
