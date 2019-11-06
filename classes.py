'''
Reference: https://github.com/bradtraversy/python_sandbox
'''
from datetime import datetime

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class

class Person:
    year = datetime.now().year
    # Constructor

    def __init__(self, name, email, birthday):
        self.name = name
        self.email = email
        self.birthday = birthday
        print('Person __init__() method was called!')

    def greeting(self):
        return 'My name is {} and I am {}'.format(self.name, self.get_age())

    def get_age(self):
        return (self.year - self.birthday)
        # Extend class

class Student(Person):
    # Constructor
    def __init__(self, name, email, birthday, class_team):
        super().__init__(name, email, birthday)
        self.class_team = class_team
        print('Student __init__() method was called before Person!')

    def get_class(self):
        return self.class_team

    def greeting(self):
        return 'My name is {} and I am {} and my class is {}'.format(self.name, self.get_age(), self.class_team)


# Init Person object
brad = Person('Brad Traversy', 'brad.traversy@gmail.com', 1989)

print('\n-- Manipulating Objects --')
print('brad.name = {}'.format(brad.name)) # Access object attributes
print('brad.email = {}'.format(brad.email))

brad.email = 'brad@gmail.com'

print('brad.email Updated = {}'.format(brad.email))
print('brad.get_age() = {}\n'.format(brad.get_age()))
print(brad.greeting())

print('\n')

# Init Student object
print('Student Object')
john = Student('John Johnson', 'john@yahoo.com', 2000, 'INFO20')

print(john.greeting())
print('{} Class Team: {}\n'.format(john.name, john.get_class()))