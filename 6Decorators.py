"""Decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the 
argument into another function and then called inside the wrapper function."""

"""Functions are 'first class objects':
-A function is an instance of the Object type.
-You can store the function in a variable.
-You can pass the function as a parameter to another function.
-You can return the function from a function.
-You can store them in data structures such as hash tables, lists, …
https://www.geeksforgeeks.org/decorators-in-python/
"""

# Function way of decorator
def hello_decorator(func):

    def inner():
        print("------Hello from inner function------")
        func()
        print("------Bye from inner function--------")

    return inner

def param_func():
    print("This is param func")

param_func = hello_decorator(param_func)
param_func()


# Using decorator way @
@hello_decorator
def param_func1():
    print("Hello there from decoration example")

param_func1()

# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        print(f"x from decor1 : {x}")
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        print(f"x from decor : {x}")
        return 2 * x 
    return inner 

@decor1
@decor
def num(): #decor1(decor(num)) => x = decor(num) then decor1(x)
    return 10

@decor
@decor1
def num2(): #decor(decor1(num2))
    return 10

print(num()) 
print(num2())

'''def div(a,b):
	return a/b
Write a decorator if a<b then swap the arguments?'''
def swap(func):
    def new(a, b):
        if(a<b):
            a, b = b, a
        return a, b
    return func

@swap
def div(a,b):
	return a/b

result = div(5, 10)
print(result)   #Swap is not working properly
