class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        result = self.__cpu * self.__memory  # Арифметические вычисления
        print(f"The result of computation with cpu and memory: {self.__cpu} * {self.__memory} = {result}")

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __str__(self):
        return f'CPU: {self.__cpu}, Memory: {self.__memory}'

class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list
        
    @property
    def sim_card_list(self):
        return self.__sim_card_list
    
    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        sim_card_name = self.sim_card_list[sim_card_number - 1]
        print(f'You are calling to number: {call_to_number}, by sim card {sim_card_number}-{sim_card_name}')

    def __str__(self):
        return f'List of sim card in this phone: {self.__sim_card_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory,sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)


    def use_gps(self, location):
        print(f'You are using GPS to get to : {location}')

    def __str__(self):
        return f'Cpu: {self.cpu}, Memory: {self.memory}, List of sim card in this phone: {self.sim_card_list}'



my_computer = Computer(18, 256)
print(my_computer)

my_phone = Phone(['Beeline', 'Mega'])
print(my_phone)

smartphone1 = SmartPhone(16, 512, ['Mega', 'O!'])
smartphone2 = SmartPhone(36, 216, ['Beeline', 'O!'])
print(smartphone1)
print(smartphone2)


my_computer.make_computations()
my_phone.call(1,996709906629)
smartphone1.use_gps('Tokmok')

print(f'Computer and smartphone has equal size of memory: {my_computer==smartphone1}')
"""done"""
