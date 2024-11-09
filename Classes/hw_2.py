class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError('This method should be implemented in derived class')

    def info(self):
        raise NotImplementedError('This method should be implemented in derived class')

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        print(f' Square Side length: {self.__side_length}{Figure.unit}, Area: {self.calculate_area()}{Figure.unit}²')

class Rectangle(Figure):
    def __init__(self, width, length):
        super().__init__()
        self.__width = width
        self.__length = length

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        print(f'Rectangle Width: {self.__width}{figure.unit}, Length: {self.__length}{Figure.unit}, Area: {self.calculate_area()}{Figure.unit}²')


square_1=Square(5)
square_2=Square(4)
rectangle_1=Rectangle(3,4)
rectangle_2=Rectangle(4,3)
rectangle_3=Rectangle(5,9)

figure_list = [square_1, square_2, rectangle_1, rectangle_2, rectangle_3]
for figure in figure_list:
    figure.info()