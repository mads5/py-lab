import sys

def greet(name):
    print(f"Your name {name} is {len(name)} characters long",end="!")
    print() #Added for newline

if __name__ == "__main__":
    name = input("Enter your name : ")
    greet(name)


def training():
    x = "Hello"[1]      # A string can be treated like a list of characters
    print("X :"+x)
    print(None)
    sum = 100 + 5000 + 5000 + \
        4000
    print(sum)

def quote_test():
    quote_str = '''hello 
    there'''
    print(quote_str)
    print(type(quote_str))

def math_expr():
    print(20/5)
    print(True * 7)
    print(False - 5)
    print(bool(-5))

def condition_test():
    ternary_op = "yay!" if bool(3) else "nay!"
    print(ternary_op)


#training()
#quote_test()
#math_expr()
condition_test()