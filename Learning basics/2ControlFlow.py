x = 0

#An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
if(x < 0):
    print("x is less than 0")
elif(x == 0):
    print("x is equal to zero")

#Ternary operator Python
result = "Negative" if x<0 else "Positive" 
print(f"result is {result}")

# ways the object returned by range() behaves as if it is a list, but in fact it isn’t. 
# It is an object which returns the successive items of the desired sequence when you iterate over it, 
# but it doesn’t really make the list, thus saving space. We say such an object is iterable.
print(range(5))
print(sum(range(5)))    # Can apply these functions on iterable
print(len(range(5)))    # Can apply these functions on iterable


# Match statements
def http_error(status):
    '''This is docstring - Control flow 'match' similar to switch case'''
    match status:
        case 400:
            print("Bad request")
            print("Hello from bad request")
            print("Hello, how are you? from bad request")
        case 401:
            print("Page not found")
        case _:
            print("Something is wrong with your internet")

http_error(601)
print(f"Doc string print : {http_error.__doc__}")


def func_annotation(ham:str, eggs:str='eggs') -> str:
    '''Function annotations'''
    print(f"Function annotations : {func_annotation.__annotations__}")
    return ham+' and '+eggs
    
f = func_annotation("burger")
print(f)