"""
'Annotations' are a way to attach metadata to function arguments and return values using the : and -> syntax. They don’t change the function behavior.
*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)
Pass by Reference - In Python every variable name is a 'reference'. When we pass a variable to a function Python, a new reference to the object is created
"""

## Annotation example
def greet(name: str, age: int) -> str:
    return f"Hello, {name} with age {age}"
g = greet("Saurangi", 32)
print(g)
print(greet.__annotations__)

## Example of args and kwards
def example_args(one, *args):
    print(one)
    for i in args:
        print(i)
example_args("Hello", "how", "are", "you")

def example_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(f"key: {k} with Value: {v}")
dict1 = dict(name = "Sdwbdb", age=32)
example_kwargs(**dict1)

## Lambda functions
def find_cube(num): return num * num * num
print(find_cube(3))
#OR
cube = lambda x: x * x * x
print(cube(2))

## Pass by reference
def myFun(x):
    x[0] = 20

li1 = [10, 11, 12, 13, 14, 15]
myFun(li1)
print(li1)

# When we pass a reference and change the received reference to something else, the connection between the passed and received parameters is broken
def swap(x, y):
    temp = x
    x = y
    y = temp
    print(f"swapped val x : {x} and y : {y}")

# Driver code
x = 2
y = 3
swap(x, y)
print(f"Original val not changed after swapping outside func, x : {x} and y : {y}")