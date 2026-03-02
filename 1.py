class Person:
    def __init__(self, name, surname):
        print('Вызов метода __init__() класса Person')
        self.name = name
        self.surname = surname

class Student(Person):
    def __init__(self, name, surname):
        print('Вызов метода __init__() класса Student')
        self.name = name
        self.surname = surname

class StanfordStudent(Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.university = 'Stanford'


student = StanfordStudent('Elon', 'Musk')