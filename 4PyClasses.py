"""Class definitions, like function definitions (def statements) must be executed before they have any effect. """

"""Mutable objects like list,dict should not be used as a class variable because just a single list would be shared by all instances -> Initialize them in __init__() rather"""
class Dog:
    purpose = "testing"

    def __init__(self, name) -> None:
        self.name = name
        self.tricks = []
    
    def add_tricks(self, tricks):
        self.tricks.append(tricks)

d = Dog("Fubby")
e = Dog("Ace")

d.add_tricks("Zoomiees")
e.add_tricks("Catch ball")

print(d.name)
print(d.tricks)
print(d.purpose)

print(e.name)
print(e.tricks)
e.purpose = "training"  # Can be initialized here as well
e.new_attribute = "xyz" # People can stamp their own data attributes as well which Python can not control
print(e.purpose)
print(e.new_attribute)

print(d.purpose)
#print(d.new_attribute)
