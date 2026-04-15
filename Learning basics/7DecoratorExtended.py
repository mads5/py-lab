#Write a division function. Write a decorator to swap both numbers if 2nd number is greater than first.

def swap_decor(func):
    
    def wrapper(a, b):
        if(b > a):
            a, b = b, a
        elif(b == 0):
            print("Cannot divide by 0")
            return
        return func(a, b)
    
    return wrapper

@swap_decor
def div(a, b):
    return a/b

result = div(50, 100)
print(result)
div(10,0)

# Decorator chaining
def add_percent(func):
    def wrapper(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return wrapper

def add_star(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
        return
    return wrapper

@add_percent
@add_star
def show_message(msg):
    print(msg)

show_message("Hello")