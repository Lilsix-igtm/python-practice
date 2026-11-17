class car:
    pass
# class tells Python that we're creating a class.
# Student is the name we've given our class.
# : tells Python that the class body starts underneath.
#pass tells Python: "There is nothing inside this class yet, but don't give me an error."

car1 = car()
car2 = car()
# car1 is the variable where we'll keep our object.
# = assigns the object to that variable.
# car() tells Python to create a new object using our Student class.
# () are used when creating the object.

print(car1)
print(car2)

#ATTRIBUTES
#they are the necessary information we add to the class objects.
car1.name = 'Ada'
car1.age = 20
car1.course = 'Accounting'

car2.name = 'Adaeze'
car2.age = 200
car2.course = 'Economics'

print(car1.name)
print(car1.age)
print(car1.course)

print(car2.name)
print(car2.age)
print(car2.course)

#OOP __init__() method
#__init__() is a special method in Python that automatically runs when you create a new object.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student('Mike', 19, 'Accountancy')

print(student1.name)
print(student1.age)
print(student1.course)

#self.name = name means:
#"Take the brand provided for that name parameter during registration and save it as an attribute called brand on this phone."

#def __init__(self, name, age, course):
#"When somebody creates a new phone object, collect its brand, model, price and colour."

class Phone:
    def __init__(self, brand, model, gen):
        self.brand = brand
        self.model = model
        self.gen = gen

    def introduction(self):
        print(f'This is {self.brand}')

    
phone1 = Phone('Iphone', '15', 8)
phone2 = Phone('Samsung', 'S25 ultra', 8)

phone1.introduction()
phone2.introduction()