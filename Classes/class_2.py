#17.04
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    """getter and setter methods"""
    def get_age(self):
        return self.__age
    def set_age(self, age):   #чтобы можно было использовать индивидуально и менять
        if type(age) == int and age>0:
         self.__age = age

        else:
            raise ValueError('Wrong value for age, must be a positive number')

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name



    def info(self):
        return f'Name: {self.__name}, Age: {self.__age}, Birth Year: {2024-self.__age}'

class Fish(Animal):
    def __init__(self, name, age):
        super(Fish, self).__init__(name, age)
    def make_voice(self):
       pass
class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)
    def make_voice(self):
        print('Meow')

class Dog(Animal):
    def __init__(self, name, age, commands):
        # super().__init__(name, age)
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property    #getter
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info()+ f', Commands: {self.__commands}'

    def make_voice(self):
        print('woof')

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins
        
    @property
    def wins(self):
        return self.__wins
    
    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info()+ f', Wins: {self.__wins}'

    def make_voice(self):
        print('Rrr, woof')
# some_animal = Animal('Anim', 3)
# # some_animal.age='Five years old'---->> #не будет работать, потомучто там есть '__'
# some_animal.set_age(4)
# print(some_animal.info())

cat= Cat('Tom', 5)
# print(cat.info())

dog = Dog('Snoopy', 3, 'sit')
dog.commands = 'sit, run'
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Reks', 5, 'fight', 3)
# print(fighting_dog.info())

fish = Fish('Nemo', 2)
animals_list = [cat, dog, fighting_dog, fish]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()

