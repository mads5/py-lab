'''
A class method in Python is defined using the @classmethod decorator and takes cls as its first parameter, 
which refers to the class itself.
A static method in Python is defined using the @staticmethod decorator and does not take any special 
first parameter (neither self nor cls).
Both can be called with Class object or directly with class name
'''

# Class method - Mostly used for Factory design
class Person:
    @classmethod
    def get_class_name(cls):
        print(f"Class method called from {cls.__name__}")

Person.get_class_name()

# Static method - Mostly used for utility functions
class Utility:
    @staticmethod
    def welcome():
        print("Static method called")

Utility.welcome()

'''Property decorator Python'''
#https://www.geeksforgeeks.org/python-property-decorator-property/