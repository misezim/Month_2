class Person:
    def __init__(self,full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Hi, my name is {self.full_name.title()}, I am {self.age} years old, and I am {self.is_married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks


    def gpa(self):
        average = round(sum(self.marks.values()) / len(self.marks),2)
        return average

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
     bonus_years = self.experience - 3
     if bonus_years > 0:
      salary = self.base_salary * (1 + 0.05 * bonus_years)
     else:
         salary = self.base_salary
     return salary

my_teacher=Teacher('aisezim', 21, 'single', 2)
my_teacher.introduce_myself()
print(f'My experience is {my_teacher.experience} years, and salary is {my_teacher.salary()}')

def create_students():
    students = [
        Student("Bob Marley", 16, 'single', {"math": 78, "physics": 90}),
        Student("Leonardo Kasper", 15, 'single', {"math": 89, "physics": 100}),
        Student("Nelson Mandela", 17, 'single', {"math": 80, "physics": 93}),
    ]
    return students

students = create_students()
for item in students:
    item.introduce_myself()
    print(f"My marks: {item.marks}")
    print(f"GPA: {item.gpa()}\n")

