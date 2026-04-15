"""if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively 
if the base class itself is derived from some other class.
This script also describes method overriding of 'print_something' with inheritance"""
'''OOPs:
Yes, Python fully supports object-oriented programming (OOP) concepts. Classes, objects, inheritance, 
encapsulation, and polymorphism are fundamental features of Python.
'''
class Animal:
    def __init__(self):
        pass
    def print_something(self):
        print("I am a Animal base class")

class Dog(Animal):
    def __init__(self):
        #Creating a private variable
        self.__c = "Private"
        self.k = "Non-private"
    def print_something(self):
        print("I am a Dog class")
    def call_super(self):
        super().print_something()
    def print_private(self):
        print(self.__c)

class Cat(Animal):
    def __init__(self):
        pass
    def print_something(self):
        print("I am a Cat class")

d = Dog()
d.print_something()
print(isinstance(d, Dog))
print(issubclass(Dog, Animal))

# Calling the method of superclass
d.call_super()
d.print_private()
print(d.k)      #Non-private variable gets accessed directly and we can change its value as well
#print(d.__c)   Attribute error when trying to access private variable of a class, cant modify its value as well

"""Python also supports multiple Inheritance - If the attribute is not found in class, it would be serached first 
in Dog class then in Cat class(left to right)"""
class A(Dog, Cat):
    pass
