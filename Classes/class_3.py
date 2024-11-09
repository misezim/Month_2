class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

"""Super Class"""
class Car:
    def __init__(self, model, year, owner):
        self.__model = model
        self.__year = year
        if type(owner) == Person:
         self.__owner = owner

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def model(self):
        return self.__model
    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model}  is driving')

    def __str__(self):      #----->magic method
        return f'MODEL:{self.__model}, YEAR:{self.__year}, OWNER:{self.__owner.name}'

    def __lt__(self, other):
        return self.year < other.year
    def __gt__(self, other):
        return self.year > other.year
    def __eq__(self, other):
        return self.year == other.year
    def __le__(self, other):
        return self.year <= other.year
    def __ge__(self, other):
        return self.year >= other.year
    def __ne__(self, other):
        return self.year != other.year


"""Small class"""
class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'Ai-95'

    @classmethod
    def buy_fuel(cls, amount):
        # FuelCar.__total_fuel += amount
        cls.__total_fuel += amount
        print(cls.print_total_fuel())

    @classmethod
    def print_total_fuel(cls):
        print(f'Factory ABC has {cls.__total_fuel} litters')

    def __init__(self, model, year, fuel_bank, owner):
        # super(FuelCar, self).__init__(model, year)
        Car.__init__(self, model, year, owner)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__()+f', FUEL BANK:{self.__fuel_bank}'

    def __add__(self, other):
       return self.__fuel_bank + other.__fuel_bank

"""small class"""
class ElectricCar(Car):
    def __init__(self, model, year, battery, owner):
        Car.__init__(self, model, year, owner)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by battery')

    def __str__(self):
        return super().__str__()+f', BATTERY:{self.__battery}'




"""mixed class"""
class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, fuel_bank, battery, owner):
        FuelCar.__init__(self, model, year, fuel_bank, owner)
        ElectricCar.__init__(self, model, year, battery, owner)

# some_car = Car('Ford', '2021')
# print(some_car)
FuelCar.buy_fuel(500)
my_friend = Person('Jim', 25)
fuel_car = FuelCar('BMW', 2021, 75, my_friend)
print(fuel_car)

electric_car=ElectricCar('Tesla', 2020, 25000, my_friend)
print(electric_car)

hybrid_car=HybridCar('Prius', 2015, 60, 15000, Person('Bob', 30))
print(hybrid_car)
hybrid_car.drive()

"""print(HybridCar.mro())""" #method resolution order- по какой очередности приоритет

print(f'Fuel car is worse that Hybrid Car: {fuel_car < hybrid_car}')
print(hybrid_car+fuel_car)
# FuelCar.__total_fuel -=100
FuelCar.print_total_fuel()
print(f'Factory ABC uses {FuelCar.get_fuel_type()}')
print(f'Owner of fuel car was born in {2024-fuel_car.owner.age}')